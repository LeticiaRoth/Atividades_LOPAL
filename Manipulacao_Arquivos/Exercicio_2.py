import pandas as pd

df = pd.read_excel("lista_pedidos.xlsx")
df.to_csv("lista_pedidos.csv", index=False)


