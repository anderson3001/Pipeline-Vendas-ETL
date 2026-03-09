import pandas as pd
import requests

print("Conectando à API para extração de dados...")
url = "https://dummyjson.com/carts"
response = requests.get(url)

if response.status_code == 200:
    dados_json = response.json()
    print("Dados extraídos com sucesso da API!")
else: 
    print(f"Falha na extração de dados. Status code: {response.status_code}")
    exit()

print("Lidando com os dados extraídos...")

linhas_pedidos = []

for carrinho in dados_json["carts"]:
    id_pedido = carrinho["id"]

    for produto in carrinho["products"]:
        linhas_pedidos.append({
            "id_pedido": id_pedido,
            "produto": produto["title"],
            "quantidade": produto["quantity"],
            "valor_unitario": produto["price"],
            "valor_total": produto["quantity"] * produto["price"]
        })

df = pd.DataFrame(linhas_pedidos)

print("Padronizando e transformando os dados...")
df["produto"] = df["produto"].str.upper()
df = df[df["quantidade"] > 0]

df.to_csv("./data/processed/pedidos_api.csv", index=False)

print(f"Pipeline concluído! {len(df)} itens processados!")