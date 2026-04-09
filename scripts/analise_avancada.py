import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

print("Iniciando Análise Avançada de Dados...")

df = pd.read_csv("../data/processed/pedidos_limpos.csv")

print("\n--- Aplicando Estatísitica ---")

media = np.mean(df["valor_total"])
desvio_padrao = np.std(df["valor_total"])

limite_superior = media + (3 * desvio_padrao)

vendas_atipicas = df[df["valor_total"] > limite_superior]

print(f"O ticket médio é de R$ {media: .2f}.")
print(f"Foram encontradas {len(vendas_atipicas)} vendas com valor absurdamentes altos (acima de {limite_superior: .2f}).")

print("\n ---- Modelo de Machine Learning ---")

dados_ml = df[["quantidade", "valor_total"]]

modelo_kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df["perfil_compra"] = modelo_kmeans.fit_predict(dados_ml)
print("Pedidos segmentados com sucesso em 3 clusters!")

print("\n --- Gerando Visualizações ---")
plt.figure(figsize=(10,6))

scatter = plt.scatter(df["quantidade"], df["valor_total"], c=df["perfil_compra"], cmap="viridis", alpha=0.6)

plt.title("Segmentação de Perfis de Compra com Machine Learning")
plt.xlabel("Quantidade de Itens no Pedido")
plt.ylabel("Valor Total do Pedido (R$)")
plt.grid(True, linestyle="--", alpha=0.5)

plt.savefig('../dashboard/grafico_clusters.png')
print("Gráfico salvo com sucesso na pasta dashboard!")


plt.show()