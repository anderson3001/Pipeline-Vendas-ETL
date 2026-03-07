import pandas as pd
from datetime import datetime
# ETL = Extract, Transform, Load
print("Iniciando extração de dados...")

df = pd.read_csv("./data/raw/pedidos_brutos.csv")

print("Iniciando transformação de dados...")

df = df.dropna() # removendo linhas em branco
df.columns = ["id_pedido", "data", "produto", "categoria", "quantidade", "valor_unitario"] # padronizando nomes das colunas
df["data"] = pd.to_datetime(df["data"]) # convertendo coluna de data para formato datetime
df["valor_total"] = df["quantidade"] * df["valor_unitario"] # calculando valor total do pedido
df = df[df["quantidade"] > 0] # removendo pedidos com quantidade inválida

print("Carregando dados transformados para arquivo final...")
df.to_csv("./data/processed/pedidos_limpos.csv", index=False)

print("Pipeline ETL concluída com sucesso!")
