import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df_vendas = pd.read_excel("vendas.xlsx")

df_vendas['total_vendas'] = df_vendas['qtd_vendida'] * df_vendas['preco_unitario']

df_vendas_por_produto = df_vendas.groupby('produto')['total_vendas'].sum().reset_index()

x = np.array(df_vendas_por_produto["produto"])
y = np.array(df_vendas_por_produto["total_vendas"])

barras = plt.bar(x, y, color='green')

plt.bar_label(barras, labels=[f'R$ {valor:,.2f}' for valor in y], padding=3, fontsize=10)

plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.title("Total de Vendas por Produto")
plt.ylabel("Valor Total (R$)")
plt.xlabel("Produto")
plt.show()
