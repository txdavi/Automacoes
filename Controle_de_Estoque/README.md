# 📦 Alerta de Reposição de Estoque com Python

Este é um projeto simples de automação com Python, ideal para freelancers que desejam praticar automações com e-commerce ou pequenos negócios. O script lê uma planilha de estoque, identifica produtos com quantidade abaixo do estoque mínimo e gera um relatório Excel com os produtos que precisam de reposição.

---

## ✅ Funcionalidades

- Leitura de planilha Excel com dados de estoque
- Verificação automática de produtos com estoque abaixo do mínimo
- Geração de relatório em Excel com produtos que precisam ser repostos

---

## 📁 Estrutura esperada do arquivo `produtos.xlsx`

O arquivo Excel deve conter as seguintes colunas:

| produto       | quantidade_atual | estoque_minimo |
|---------------|------------------|----------------|
| Mouse Gamer   | 3                | 10             |
| Teclado       | 5                | 4              |
| Monitor 24"   | 2                | 3              |

---

## 💻 Como usar

1. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

2. Coloque seu arquivo `produtos.xlsx` na mesma pasta do script.

3. Execute o script Python.

4. Será gerado um arquivo `alerta_reposicao.xlsx` com os produtos que precisam de reposição.

---

## 📦 Requisitos

- Python 3.x
- Pandas
- openpyxl (para manipulação de arquivos .xlsx)

---

## 📜 Licença

Este projeto é de uso livre para fins educacionais e comerciais.
