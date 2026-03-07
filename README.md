# 📊 Pipeline ETL de E-commerce: Do Script ao Dashboard

Este projeto prático foi desenvolvido para explorar o ciclo de vida completo dos dados, conectando a geração de registros transacionais com a análise de Business Intelligence. 

Como desenvolvedor, estou acostumado a estruturar a criação de dados no back-end (pedidos, itens, clientes). O objetivo aqui foi dar o próximo passo: entender como extrair, limpar e modelar esses dados brutos para gerar valor analítico.

## 🚀 O Projeto

O projeto simula o fluxo de dados de um e-commerce e é dividido em três etapas principais:

1. **Geração de Dados (Mock):** Um script em Python puro que gera um arquivo CSV com milhares de transações simuladas, injetando intencionalmente "ruídos" e inconsistências comuns no mundo real (valores nulos, quantidades negativas, falhas de formatação).
2. **Processamento e ETL:** Um pipeline construído com Python e a biblioteca **Pandas**. O script extrai os dados brutos, realiza a sanitização, aplica regras de negócio (criação de colunas calculadas) e carrega o dado processado.
3. **Visualização:** Um dashboard interativo no **Power BI** consumindo os dados limpos, utilizando modelagem simples e métricas criadas com linguagem **DAX** para analisar o faturamento e o volume de vendas.

## 🛠️ Tecnologias Utilizadas

* **Python 3:** Lógica de geração de dados e automação.
* **Pandas:** Manipulação de DataFrames, limpeza e transformação de dados (ETL).
* **Power BI:** Conexão de dados, criação de visuais e segmentação.
* **DAX:** Criação de medidas calculadas (ex: contagem distinta de pedidos).
* **Git/GitHub:** Versionamento de código pelo terminal.

## 📁 Estrutura do Repositório

```text
├── data/
│   ├── raw/                      # Dados brutos com inconsistências gerados pelo script
│   └── processed/                # Dados sanitizados prontos para consumo do BI
├── scripts/
│   ├── gerador_dados.py          # Script gerador de transações
│   └── etl_pipeline.py           # Script principal de ETL com Pandas
└── dashboard/                    
    └── analise_vendas.pbix       # Painel interativo do Power BI
```
## ⚙️ Como executar

Os arquivos de dados brutos e processados já estão disponíveis nas pastas correspondentes para facilitar a visualização no Power BI. Porém, se você quiser testar o pipeline do zero, siga os passos abaixo:

1. Clone o repositório para a sua máquina.
2. Certifique-se de ter o Python e a biblioteca Pandas instalados (`pip install pandas`).
3. Navegue até a pasta `scripts/`.
4. Rode `python gerador_dados.py` para criar uma nova base de dados suja e aleatória na pasta `data/raw/`.
5. Rode `python etl_pipeline.py` para executar o processo de extração, limpeza e transformação. O novo arquivo limpo substituirá o antigo na pasta `data/processed/`.
6. Abra o arquivo `.pbix` na pasta `dashboard/` e clique em "Atualizar" no Power BI para ver os gráficos refletirem os novos dados processados.


***
