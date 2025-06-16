# Verificador de Distorção de Idade Escolar

Este projeto em Python analisa uma planilha com dados de alunos para identificar possíveis casos de **distorção idade-série** — quando um aluno está com uma idade incompatível com o ano escolar frequentado.

## 📋 Requisitos

- Python 3.7+
- `pandas`
- `openpyxl` (para leitura de arquivos .xlsx)

## 📁 Entrada de Dados

O programa espera um arquivo chamado `base_dados.xlsx` no mesmo diretório, contendo as colunas:

- `Nome`
- `Data de Nascimento`
- `Ano de escolaridade`
- `Data de Matricula`

## 📊 Como Funciona

1. Lê os dados de um arquivo `.xlsx`;
2. Calcula a idade dos alunos com base no ano letivo;
3. Filtra alunos com mais de 2 anos de atraso escolar;
4. Exibe os dados dos alunos com possível distorção idade-série.

## ▶️ Como Executar

```bash
pip install -r requirements.txt
python main.py
```

## ✅ Exemplo de Saída

```
         Nome  Idade Ano de escolaridade
0  João Silva     12               4º Ano
1  Maria Souza    13               5º Ano
```

## 📌 Observações
- Os anos de escolaridade analisados são 4º e 5º ano
- O ano letivo analisado é 2022. Para atualizar, altere a variável `ano_letivo` no script.
- Certifique-se de que as datas estejam corretamente formatadas no Excel.
