# Importa a biblioteca pandas para manipulação de dados
import pandas as pd

# Define o nome do arquivo Excel que contém a base de dados
arquivo = 'base_dados.xlsx'

# Carrega o arquivo Excel para um DataFrame
df = pd.read_excel(arquivo)

# Define o ano letivo e o ano de escolaridade que serão considerados para calcular a distorção de idade dos alunos
ano_letivo = 2022
ano_escolaridade = "5º ANO"

# Seleciona apenas as colunas necessárias da base de dados
df = df[['Nome', 'Data de Nascimento', 'Ano de escolaridade', 'Data de Matricula']]

# Converte a coluna 'Data de Matricula' para o formato de data normal (datetime)
df['Data de Matricula'] = pd.to_datetime(df['Data de Matricula'])

#Converte o ano de escolaridade da tabela para Upper
df['Ano de escolaridade'] = df['Ano de escolaridade'].str.upper()

df['Idade'] = ano_letivo - pd.to_datetime(df['Data de Nascimento']).dt.year
distorcidos = df[(df['Idade'] > 12) & (df['Ano de escolaridade'] == ano_escolaridade)]

if not distorcidos.empty:
    print(distorcidos[['Nome', 'Idade','Ano de escolaridade']])
else:
    print("Não há alunos com distorção de idade")

