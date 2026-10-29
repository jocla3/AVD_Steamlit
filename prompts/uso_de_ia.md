# Declaração de uso de IA

**Ferramenta:** Claude Code (Anthropic).

## Prompt principal

> Com base na sua EDA, crie uma aplicação no Streamlit com dois dashboards.
> - Dashboard 1: um "laboratório" de análise de distribuição e correlação
> - Dashboard 2: KPIs e métricas voltadas a um público alvo determinado individualmente
>
> Visuais mínimos — painel lateral: 1 seletor de variáveis e 1 filtro de intervalo (slider);
> Dashboard 1: mapa de calor de correlação e um histograma por variável quantitativa;
> Dashboard 2: 3 a 5 métricas próprias e 3 visuais.
> Entregáveis: notebooks, app.py, entregas/ (rascunhos dos dois dashboards) e prompts/.
> Dataset: https://www.kaggle.com/datasets/jethwaaatmik/telco-customer-churn-dataset

## Para que foi usada
- Gerar o esqueleto do `app.py` (carga e tratamento dos dados, painel lateral, abas, gráficos Plotly).
- Escrever os rascunhos de layout em `entregas/`.
- Testar automaticamente todos os widgets com `streamlit.testing.AppTest`.

## O que foi aceito / modificado / rejeitado
- _Preencher:_ ex.: aceito o tratamento de ausentes; modificado o público-alvo do dashboard 2; rejeitado …
