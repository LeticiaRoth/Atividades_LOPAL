import pandas as pd

df =pd.read_csv("lista_pedidos.csv")
df.to_json("lista_pedidos.json", index=False)


