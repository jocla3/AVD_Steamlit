# AVD — Telco Churn em Streamlit

Trabalho de faculdade (disciplina AVD): dois dashboards Streamlit sobre o dataset Telco Customer Churn (Kaggle, 7.043 clientes).
App publicado no Streamlit Community Cloud a partir da branch `main` deste repositório (`jocla3/AVD_Steamlit`) — push em `main` publica.

## Rodar

```bash
.venv/bin/streamlit run app.py
```

Porta 8501. O ambiente virtual já existe em `.venv/`; dependência nova vai em `requirements.txt` com versão fixada (o Streamlit Cloud instala a partir dele).

## Estrutura

- `app.py` — app inteiro (carga e tratamento em `carregar_dados()`, painel lateral, duas abas).
- `data/telco_data.csv` — dataset, lido por caminho relativo: rodar sempre a partir da raiz.
- `notebooks/Aula_11_Pratica_EDA.ipynb` — EDA que definiu o tratamento de dados.
- `entregas/` — rascunhos dos dois dashboards entregues.
- `prompts/uso_de_ia.md` — declaração de uso de IA exigida pela disciplina; atualizar quando a IA mudar algo relevante.

## Regras

- Tratamento de dados do app deve continuar igual ao do notebook (ver README, seção "Tratamento de dados"). Mudou um, mude o outro.
- `customerID` sai na carga e o app só mostra agregados — nunca exibir linha individual.
- Interface e textos em PT-BR; rótulos de churn são "Sim"/"Não".
- Paleta: cinza `#c9c9c9` para contexto, roxo `#7b2cbf` para destaque (churn).
- Sem testes automatizados: verificar abrindo o app e conferindo as duas abas.
