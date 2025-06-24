import pandas as pd
import datetime

hoje = pd.Timestamp(datetime.datetime.today().date())

def verifica_status(row):
    data_prevista = row['data_entrega_prevista']
    data_entregue = row['data_entregue']

    # Se data_entregue for NaT e data_prevista for menor que a data de hoje → Atrasado
    if pd.isna(data_entregue) and data_prevista < hoje:
        return "Atrasado"

    # Se data_entregue > data_prevista → Entregue com atraso
    elif pd.notna(data_entregue) and data_entregue > data_prevista:
        return "Entregue com atraso"

    # Caso contrário → Entregue no prazo
    else:
        return "Entregue no prazo"



df_pedidos = pd.read_excel('pedidos.xlsx')

df_pedidos['data_entrega_prevista'] = pd.to_datetime(df_pedidos['data_entrega_prevista'])
df_pedidos['data_entregue'] = pd.to_datetime(df_pedidos['data_entregue'], errors='coerce')

df_pedidos['status_entrega'] = df_pedidos.apply(verifica_status, axis=1)

df_pedidos.to_excel('relatorio_entregas.xlsx', index=False)
