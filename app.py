import numpy as np
import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="Telco Churn — Dashboards", page_icon="📡", layout="wide")

COR_CONTEXTO = "#c9c9c9"
COR_DESTAQUE = "#7b2cbf"
CORES_CHURN = {"Não": COR_CONTEXTO, "Sim": COR_DESTAQUE}

VARS_QUANT = {
    "tenure": "Tempo de contrato (meses)",
    "MonthlyCharges": "Mensalidade (US$)",
    "TotalCharges": "Total faturado (US$)",
}


@st.cache_data
def carregar_dados():
    df = pd.read_csv("data/telco_data.csv")
    # customerID é identificador pessoal e não agrega à análise: sai logo na carga
    df = df.drop(columns="customerID")

    # Mesmo tratamento decidido na EDA
    df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
    df.loc[df["tenure"] == 0, "TotalCharges"] = df.loc[df["tenure"] == 0, "TotalCharges"].fillna(0)
    # tenure e MonthlyCharges ausentes: reconstrói pela relação TotalCharges ≈ tenure × MonthlyCharges,
    # e o que sobrar vai para a mediana (variáveis assimétricas)
    df["tenure"] = df["tenure"].fillna((df["TotalCharges"] / df["MonthlyCharges"]).round().clip(upper=72))
    df["MonthlyCharges"] = df["MonthlyCharges"].fillna(df["TotalCharges"] / df["tenure"].replace(0, np.nan))
    for col in VARS_QUANT:
        df[col] = df[col].fillna(df[col].median())
    cat_cols = df.select_dtypes(exclude="number").columns
    df[cat_cols] = df[cat_cols].fillna("Não informado")

    df["Churn"] = df["Churn"].map({"Yes": "Sim", "No": "Não"})
    df["churn_flag"] = (df["Churn"] == "Sim").astype(int)
    df["SeniorCitizen"] = df["SeniorCitizen"].map({1: "Sim", 0: "Não"})
    df["faixa_tenure"] = pd.cut(
        df["tenure"], bins=[-1, 6, 12, 24, 48, 72],
        labels=["0–6", "7–12", "13–24", "25–48", "49–72"],
    )
    return df


df_full = carregar_dados()

# ---------------- Painel lateral ----------------
st.sidebar.header("Filtros")
vars_sel = st.sidebar.multiselect(
    "Variáveis quantitativas avaliadas",
    options=list(VARS_QUANT),
    default=list(VARS_QUANT),
    format_func=VARS_QUANT.get,
)
var_filtro = st.sidebar.selectbox(
    "Variável do filtro de intervalo", options=list(VARS_QUANT), format_func=VARS_QUANT.get
)
vmin, vmax = float(df_full[var_filtro].min()), float(df_full[var_filtro].max())
intervalo = st.sidebar.slider(
    f"Intervalo de {VARS_QUANT[var_filtro]}", min_value=vmin, max_value=vmax, value=(vmin, vmax)
)
contratos = st.sidebar.multiselect(
    "Tipo de contrato",
    options=sorted(df_full["Contract"].unique()),
    default=sorted(df_full["Contract"].unique()),
)

df = df_full[df_full[var_filtro].between(*intervalo) & df_full["Contract"].isin(contratos)]
st.sidebar.caption(f"{len(df):,} de {len(df_full):,} clientes no recorte".replace(",", "."))

st.title("📡 Telco Customer Churn")

if df.empty:
    st.warning("Nenhum cliente no recorte atual. Ajuste os filtros do painel lateral.")
    st.stop()

aba_lab, aba_kpi = st.tabs(["🔬 Laboratório de distribuição e correlação", "📊 KPIs de retenção"])

# ---------------- Dashboard 1 ----------------
with aba_lab:
    st.subheader("Laboratório de distribuição e correlação")
    if not vars_sel:
        st.info("Selecione ao menos uma variável quantitativa no painel lateral.")
    else:
        c1, c2, c3 = st.columns(3)
        metodo = c1.radio(
            "Método de correlação", ["spearman", "pearson", "kendall"], horizontal=True,
            help="Spearman é o padrão: nenhuma variável passou no teste de normalidade na EDA.",
        )
        incluir_churn = c2.toggle("Incluir Churn (0/1) na matriz", value=True)
        separar = c3.toggle("Separar histogramas por Churn", value=True)
        bins = st.slider("Número de bins dos histogramas", 5, 80, 30)

        cols_corr = vars_sel + (["churn_flag"] if incluir_churn else [])
        if len(cols_corr) < 2:
            st.info("A matriz de correlação precisa de pelo menos duas variáveis.")
        else:
            corr = df[cols_corr].corr(method=metodo).rename(
                index={**VARS_QUANT, "churn_flag": "Churn"}, columns={**VARS_QUANT, "churn_flag": "Churn"}
            )
            fig = px.imshow(
                corr, text_auto=".2f", zmin=-1, zmax=1, color_continuous_scale="RdBu_r",
                title=f"Matriz de correlação ({metodo.capitalize()})",
            )
            st.plotly_chart(fig, width="stretch")

        cols = st.columns(len(vars_sel))
        for col, var in zip(cols, vars_sel):
            fig = px.histogram(
                df, x=var, nbins=bins, color="Churn" if separar else None,
                color_discrete_map=CORES_CHURN, barmode="overlay", opacity=0.75,
                labels={var: VARS_QUANT[var]}, title=VARS_QUANT[var],
            )
            if not separar:
                fig.update_traces(marker_color=COR_DESTAQUE)
            col.plotly_chart(fig, width="stretch")

        with st.expander("Estatística descritiva do recorte"):
            desc = df[vars_sel].describe().T
            desc["assimetria"] = df[vars_sel].skew()
            desc["curtose"] = df[vars_sel].kurtosis()
            st.dataframe(desc.rename(index=VARS_QUANT).round(2), width="stretch")

# ---------------- Dashboard 2 ----------------
# Público-alvo: diretoria de Retenção / Customer Success
with aba_kpi:
    st.subheader("KPIs de retenção — visão para a diretoria de Customer Success")
    churners = df[df["churn_flag"] == 1]
    ativos = df[df["churn_flag"] == 0]

    m1, m2, m3, m4, m5 = st.columns(5)
    taxa = df["churn_flag"].mean()
    taxa_base = df_full["churn_flag"].mean()
    m1.metric("Taxa de churn", f"{taxa:.1%}", f"{(taxa - taxa_base) * 100:+.1f} p.p.", delta_color="inverse")
    m2.metric("Clientes ativos", f"{len(ativos):,}".replace(",", "."))
    m3.metric("Receita mensal perdida", f"US$ {churners['MonthlyCharges'].sum() / 1000:.1f} mil")
    m4.metric("Ticket médio dos ativos", f"US$ {ativos['MonthlyCharges'].mean():.0f}" if len(ativos) else "—")
    m5.metric("Tenure médio de quem saiu", f"{churners['tenure'].mean():.0f} meses" if len(churners) else "—")

    v1, v2 = st.columns(2)
    por_contrato = df.groupby("Contract", as_index=False)["churn_flag"].mean()
    fig = px.bar(
        por_contrato.sort_values("churn_flag", ascending=False), x="Contract", y="churn_flag",
        text_auto=".1%", title="Taxa de churn por tipo de contrato",
        labels={"Contract": "Contrato", "churn_flag": "Taxa de churn"},
        color_discrete_sequence=[COR_DESTAQUE],
    )
    fig.update_yaxes(tickformat=".0%")
    v1.plotly_chart(fig, width="stretch")

    por_faixa = df.groupby("faixa_tenure", as_index=False, observed=True)["churn_flag"].mean()
    fig = px.line(
        por_faixa, x="faixa_tenure", y="churn_flag", markers=True,
        title="Taxa de churn por tempo de casa (meses)",
        labels={"faixa_tenure": "Tempo de contrato", "churn_flag": "Taxa de churn"},
        color_discrete_sequence=[COR_DESTAQUE],
    )
    fig.update_yaxes(tickformat=".0%")
    v2.plotly_chart(fig, width="stretch")

    perda_pgto = churners.groupby("PaymentMethod", as_index=False)["MonthlyCharges"].sum()
    fig = px.bar(
        perda_pgto.sort_values("MonthlyCharges"), x="MonthlyCharges", y="PaymentMethod", orientation="h",
        text_auto=",.0f", title="Receita mensal perdida por forma de pagamento (US$)",
        labels={"PaymentMethod": "", "MonthlyCharges": "US$ / mês"},
        color_discrete_sequence=[COR_DESTAQUE],
    )
    st.plotly_chart(fig, width="stretch")

    st.caption(
        "Dados: Telco Customer Churn (Kaggle). Identificadores de cliente são removidos na carga; "
        "o app exibe apenas agregados."
    )
