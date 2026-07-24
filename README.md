# 📊 Supply Chain Analytics — Análise Exploratória de Dados

> Projeto de **análise de dados** aplicado a um cenário realista de **Supply Chain /
> Demand Planning** em uma indústria de bens de consumo. A partir de dados de pedidos,
> estoque, entregas e produtos, o projeto extrai insights acionáveis para apoiar a
> tomada de decisão do negócio.

![Python](https://img.shields.io/badge/Python-3.10+-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626)

---

## 🎯 Contexto de Negócio

Como estagiário em **Demand Planning na Unilever**, faço parte da rotina de análise de
risco de ruptura, monitoramento de entregas e apoio à decisão do time de Supply Chain.
Este projeto **simula esse cenário com dados fictícios** para demonstrar, de ponta a ponta,
uma análise exploratória de dados (EDA) com foco em negócio.

> ⚠️ Todos os dados são **inteiramente fictícios**, gerados artificialmente. Nenhum dado
> real de qualquer empresa foi utilizado.

## ❓ Perguntas de Negócio Respondidas

1. **Vendas** — Quais marcas, categorias, regiões e canais mais faturam?
2. **Sazonalidade** — Como as vendas evoluem ao longo dos meses?
3. **Ruptura** — Quais SKUs estão em risco de ruptura?
4. **OTIF** — Quais marcas e transportadoras têm pior performance de entrega?
5. **SKUs críticos** — Quais produtos exigem ação imediata (alta demanda + baixo estoque)?
6. **Forecast** — Previsão simples de demanda por média móvel.

---

## 🛠️ Stack Utilizada

| Categoria | Ferramentas |
|---|---|
| Linguagem | **Python 3.10+** |
| Análise | **Pandas**, **NumPy** |
| Visualização | **Matplotlib**, **Seaborn** |
| Ambiente | **Jupyter Notebook** (ou Google Colab) |

---

## 📁 Estrutura do Projeto

```
supply-chain-analytics/
├── README.md
├── requirements.txt
├── gerar_dados.py                  # Gera os dados fictícios (CSVs)
├── data/
│   └── raw/                        # produtos, pedidos, estoque, entregas (CSV)
├── notebook/
│   └── analise_supply_chain.ipynb  # 📓 Notebook principal (a estrela do projeto)
└── docs/
    └── img/                        # Gráficos exportados da análise
```

---

## 📈 Prévia das Análises

### Análise de Vendas
![Vendas] https://github.com/banciella/Supply--Chain-Analytics/blob/main/04_vendas.png

### Matriz de Criticidade (Demanda x Estoque)
![Críticos](docs/img/08_criticos.png)

### Performance de Entrega (OTIF)
![OTIF](docs/img/07_otif.png)

---

## ▶️ Como Executar

### Opção A — Google Colab (mais fácil, sem instalar nada) ☁️

1. Acesse [Google Colab](https://colab.research.google.com/).
2. Faça upload do notebook `notebook/analise_supply_chain.ipynb`.
3. Faça upload dos 4 CSVs da pasta `data/raw/` (ou rode o `gerar_dados.py` no Colab).
4. Ajuste a variável `PATH` na segunda célula para apontar para os arquivos.
5. Rode todas as células (**Ambiente de execução → Executar tudo**).

### Opção B — Localmente (VS Code / Jupyter) 💻

```bash
# 1. Clone o repositório
git clone https://github.com/<seu-usuario>/supply-chain-analytics.git
cd supply-chain-analytics

# 2. Crie o ambiente virtual e instale as dependências
python -m venv .venv
# Windows: .venv\Scripts\activate | Linux/Mac: source .venv/bin/activate
pip install -r requirements.txt

# 3. Gere os dados fictícios
python gerar_dados.py

# 4. Abra o notebook
jupyter notebook notebook/analise_supply_chain.ipynb
```

---

## 🎯 Principais Insights

- 📦 **Cuidados Pessoais** é a categoria líder de faturamento (~64%), puxada por **Vasenol** e **Dove**.
- 🗺️ A região **Sudeste** concentra a maior fatia das vendas.
- 📈 Há **tendência de crescimento** das vendas ao longo do 1º semestre, com pico em junho.
- 🔴 Cerca de **1 em cada 5 SKUs** está abaixo do ponto de reposição na posição mais recente.
- 🚚 O **OTIF geral** gira em torno de **84%**, com variação relevante entre marcas e transportadoras.
- 🚨 A **matriz de criticidade** destaca SKUs de alto faturamento com baixa cobertura de estoque — prioridade máxima de reposição.

---

## 🚀 Próximos Passos (Roadmap)

- Substituir a média móvel por modelos de forecast mais robustos (**Prophet**, **ARIMA**).
- Migrar o processamento para **PySpark** para grandes volumes.
- Construir um **dashboard interativo** no **Power BI**.
- Automatizar a atualização dos dados com **Apache Airflow**.

---

## 👤 Autor

**Felipe Comenale Banciella**
Estagiário em Demand Planning @ Unilever · Estudante de Análise e Desenvolvimento de Sistemas (UNIP)
Em transição para Análise / Engenharia de Dados.

- 💼 [LinkedIn](https://www.linkedin.com/in/felipe-banciella)
- 🐙 [GitHub](https://github.com/felipe-banciella)
