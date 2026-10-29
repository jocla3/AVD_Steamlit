# Rascunho — Dashboard 1: Laboratório de distribuição e correlação

**Objetivo:** explorar livremente como as variáveis quantitativas se distribuem e se relacionam com o churn, reproduzindo de forma interativa as seções 3 (distribucional) e 6 (relacional) da EDA.

**Público:** analista de dados / quem fez a EDA.

```
┌──────────────── PAINEL LATERAL ────────────────┐ ┌──────────────────────── ABA "LABORATÓRIO" ────────────────────────┐
│ [multiselect] Variáveis quantitativas          │ │ (o) Spearman ( ) Pearson ( ) Kendall   [x] Incluir Churn   [x] Por │
│   tenure · MonthlyCharges · TotalCharges       │ │                                                         Churn      │
│                                                │ │ Bins: ──────●──────────                                             │
│ [select] Variável do filtro de intervalo       │ │ ┌────────────────────────────────────────────────────────────────┐ │
│                                                │ │ │              MAPA DE CALOR DE CORRELAÇÃO                       │ │
│ [slider] ●────────────────● (min–max)          │ │ │   (variáveis selecionadas + Churn 0/1, escala -1 a 1)          │ │
│                                                │ │ └────────────────────────────────────────────────────────────────┘ │
│ [multiselect] Tipo de contrato                 │ │ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐                  │
│                                                │ │ │ Histograma   │ │ Histograma   │ │ Histograma   │  ← 1 por variável │
│ "N de 7.043 clientes no recorte"               │ │ │ tenure       │ │ Monthly      │ │ Total        │    selecionada    │
└────────────────────────────────────────────────┘ │ └──────────────┘ └──────────────┘ └──────────────┘                  │
                                                   │ ▸ Estatística descritiva do recorte (média, mediana, assimetria…) │
                                                   └────────────────────────────────────────────────────────────────────┘
```

**Decisões de design**
- Spearman como padrão: na EDA nenhuma variável quantitativa passou no Shapiro-Wilk.
- Convenção de cor herdada da EDA: cinza = contexto (não churn), roxo = destaque (churn).
- O slider permite excluir faixas (ex.: clientes com tenure 0 ou mensalidades extremas) e ver o efeito na correlação.
