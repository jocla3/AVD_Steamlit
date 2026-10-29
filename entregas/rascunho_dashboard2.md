# Rascunho — Dashboard 2: KPIs de retenção

**Público-alvo:** diretoria de Retenção / Customer Success da operadora.
**Pergunta que o painel responde:** "Quanto estamos perdendo com churn, onde está concentrado e onde agir primeiro?"

```
┌──────────────────────────────────── ABA "KPIs DE RETENÇÃO" ────────────────────────────────────┐
│ ┌────────────┐ ┌────────────┐ ┌──────────────┐ ┌──────────────┐ ┌───────────────────────┐       │
│ │ Taxa de    │ │ Clientes   │ │ Receita      │ │ Ticket médio │ │ Tenure médio de quem  │       │
│ │ churn      │ │ ativos     │ │ mensal       │ │ dos ativos   │ │ saiu                  │       │
│ │ 26,5% ▲p.p.│ │ 5.174      │ │ perdida US$  │ │ US$          │ │ meses                 │       │
│ └────────────┘ └────────────┘ └──────────────┘ └──────────────┘ └───────────────────────┘       │
│ ┌───────────────────────────────────────┐ ┌───────────────────────────────────────┐             │
│ │ Barras: taxa de churn por contrato    │ │ Linha: taxa de churn por faixa de     │             │
│ │ (Month-to-month × 1 ano × 2 anos)     │ │ tempo de casa (0–6, 7–12, … 49–72)    │             │
│ └───────────────────────────────────────┘ └───────────────────────────────────────┘             │
│ ┌─────────────────────────────────────────────────────────────────────────────────┐             │
│ │ Barras horizontais: receita mensal perdida por forma de pagamento (US$)         │             │
│ └─────────────────────────────────────────────────────────────────────────────────┘             │
└─────────────────────────────────────────────────────────────────────────────────────────────────┘
```

**Métricas próprias (5)**
1. Taxa de churn — com delta em p.p. contra a base completa (vermelho quando piora).
2. Clientes ativos no recorte.
3. Receita mensal perdida — soma das mensalidades de quem cancelou (MRR em risco).
4. Ticket médio dos clientes ativos.
5. Tenure médio de quem saiu — indica em que momento da jornada o cliente vai embora.

**Visuais (3):** churn por contrato, churn por tempo de casa, receita perdida por forma de pagamento.

Todos os filtros do painel lateral também valem para esta aba.
