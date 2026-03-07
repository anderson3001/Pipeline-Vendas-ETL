import csv
import random
from datetime import datetime, timedelta

produtos = [
    ("Teclado Mecânico", "Periféricos", 350.00), ("Mouse Gamer", "Periféricos", 150.50),
    ("Monitor 24p", "Monitores", 800.00), ("Cadeira Gamer", "Móveis", 1200.00),
    ("Cabo HDMI", "Acessórios", 25.00), ("Headset", "Periféricos", 250.00)
]

data_inicial = datetime(2026, 1, 1)

with open("pedidos_brutos.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["ID Pedido", "Data", "Produto", "Categoria", "Quantidade", "Valor Unitário"])

    for i in range(1, 10001):
        produto = random.choice(produtos)

        data_compra = data_inicial + timedelta(days=random.randint(0, 365))
        qtd = random.choices([1, 2, 3, 0, -1], weights=[70, 15, 5, 5, 5])[0] # dados inválidos de propósito

        if random.randint(1, 1000) == 1:
            writer.writerow([]) # linha em branco de propósito
            continue
        
        writer.writerow([i, data_compra.strftime("%Y-%m-%d"), produto[0], produto[1], qtd, produto[2]])

print("Arquivo 'pedidos_brutos.csv' gerado com 10.000 registros!")
