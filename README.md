# Telco Customer Churn — Dashboards em Streamlit

**App publicado:** https://avdsteamlit-3xi84793sksmscqt7qpczm.streamlit.app

Aplicação construída a partir da EDA do dataset [Telco Customer Churn](https://www.kaggle.com/datasets/jethwaaatmik/telco-customer-churn-dataset) (7.043 clientes, 21 colunas).

## Dashboards
1. **Laboratório de distribuição e correlação** — mapa de calor (Spearman/Pearson/Kendall) e um histograma por variável quantitativa selecionada, com opção de separar por churn.
2. **KPIs de retenção** — para a diretoria de Customer Success: taxa de churn, clientes ativos, receita mensal perdida, ticket médio e tenure médio de quem saiu, mais três visuais.

O painel lateral (seletor de variáveis, slider de intervalo e filtro de contrato) vale para as duas abas.

## Estrutura
```
app.py                 aplicação Streamlit
data/telco_data.csv    dataset (público, Kaggle)
notebooks/             EDA
entregas/              rascunhos dos dois dashboards
prompts/               declaração de uso de IA
requirements.txt
```

## Rodando localmente
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Tratamento de dados
- `customerID` é removido na carga e nenhuma linha individual é exibida — o app mostra apenas agregados.
- `TotalCharges` convertido para número; vazio em clientes com `tenure = 0` vira 0.
- `tenure` e `MonthlyCharges` ausentes são reconstruídos pela relação `TotalCharges ≈ tenure × MonthlyCharges`; o restante recebe a mediana.
- Categóricas ausentes viram "Não informado".
