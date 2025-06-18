import pandas as pd
from pandas import DataFrame

df_estoq = pd.read_excel("produtos.xlsx")


reposicao = []
for _, row in df_estoq.iterrows():
    produtos = row["produto"]
    quantidade_atual = row["quantidade_atual"]
    estoque_minimo = row["estoque_minimo"]

    if quantidade_atual < estoque_minimo:
        reposicao.append((produtos, quantidade_atual))

df_reposicao = pd.DataFrame(reposicao, columns=['produtos', 'quantidade_atual'])

df_reposicao.to_excel('alerta_reposicao.xlsx', index=False)
