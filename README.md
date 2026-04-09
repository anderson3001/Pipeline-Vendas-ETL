# 📊 Pipeline de Dados E-commerce: Do ETL ao Machine Learning e BI

Este projeto prático foi desenvolvido para explorar o ciclo de vida completo dos dados, conectando a geração de registros transacionais com a engenharia de dados, análise estatística avançada e Business Intelligence. 

Como desenvolvedor, estou acostumado a estruturar a criação de dados no back-end (pedidos, itens, clientes). O objetivo aqui foi dar o próximo passo: entender como extrair, limpar, modelar e aplicar inteligência a esses dados brutos para gerar insights valiosos de negócio.

## 🚀 O Projeto

O projeto simula o fluxo de dados de um e-commerce e é dividido em quatro etapas principais:

1. **Geração e Ingestão de Dados:** * **Mock Local:** Um script em Python puro que gera um arquivo CSV com milhares de transações simuladas, injetando intencionalmente "ruídos" e inconsistências comuns no mundo real.
   * **Consumo de API:** Um script alternativo que simula a realidade de integração de sistemas, consumindo dados em formato JSON de uma API REST pública e achatando-os (flattening) para formato tabular.
2. **Processamento e ETL:** Um pipeline construído com Python e a biblioteca **Pandas**. O script realiza a sanitização dos dados, tratamento de valores inconsistentes, aplica tipagem correta e regras de negócio (criação de colunas calculadas).
3. **Ciência de Dados e Insights:** Aplicação de **NumPy** para análise estatística (detecção de anomalias/outliers usando a regra do Desvio Padrão) e **Scikit-Learn** para rodar um modelo de Machine Learning (**K-Means**), segmentando os clientes em perfis de compra. Os resultados foram plotados utilizando **Matplotlib**.
4. **Visualização:** Um dashboard interativo no **Power BI** consumindo os dados processados, utilizando modelagem simples e métricas criadas com linguagem **DAX** para analisar o faturamento e o volume de vendas.

## 🛠️ Tecnologias Utilizadas

* **Python 3:** Lógica de extração, automação e análise.
* **Pandas:** Limpeza e transformação de dados (ETL) e achatamento de JSONs.
* **Requests:** Consumo de APIs RESTful.
* **NumPy:** Cálculos estatísticos e detecção de outliers.
* **Scikit-Learn:** Algoritmos de clusterização de Machine Learning (K-Means).
* **Matplotlib:** Visualização de dados em código (Scatter Plots).
* **Power BI & DAX:** Visualização de negócio e métricas calculadas.
* **Git/GitHub:** Versionamento de código por linha de comando.

## 📁 Estrutura do Repositório

```text
├── data/
│   ├── raw/                      # Dados brutos com inconsistências
│   └── processed/                # Dados sanitizados prontos para consumo
├── scripts/
│   ├── gerador_dados.py          # Script gerador de transações em CSV
│   ├── etl_pipeline.py           # Script clássico de ETL com Pandas
│   ├── etl_api.py                # Pipeline de ingestão via API REST
│   └── analise_avancada.py       # Script de Estatística e Machine Learning
└── dashboard/                    
    ├── analise_vendas.pbix       # Painel interativo do Power BI
    └── grafico_clusters.png      # Output visual do modelo de IA
```
## ⚙️ Como reproduzir este projeto
Os arquivos de dados brutos e processados já estão disponíveis nas pastas correspondentes para facilitar a visualização no Power BI. Porém, se você quiser testar o pipeline do zero, siga os passos abaixo:

1. Clone o repositório para a sua máquina.

2. Certifique-se de ter as bibliotecas necessárias instaladas:

```bash
pip install pandas requests numpy matplotlib scikit-learn
```
3. Navegue até a pasta scripts/.

4. Para gerar dados: Rode python gerador_dados.py para criar uma nova base de dados suja na pasta data/raw/.

5. Para o ETL: Rode python etl_pipeline.py (ou python etl_api.py) para executar a limpeza e transformação. O arquivo limpo será gerado na pasta data/processed/.

6. Para o Machine Learning: Rode python analise_avancada.py para rodar o modelo K-Means, ver os dados estatísticos no terminal e gerar o gráfico de clusters.

7. Para o Dashboard: Abra o arquivo .pbix na pasta dashboard/ com o Power BI Desktop e clique em "Atualizar" para ver os gráficos refletirem os novos dados.

***
