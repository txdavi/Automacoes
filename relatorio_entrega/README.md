# 📦 Análise de Pedidos Atrasados com Python

Este projeto realiza uma análise automatizada de pedidos com base em prazos de entrega.

## 🔍 O que o script faz

- Lê um arquivo Excel com os pedidos
- Converte as datas para o formato correto
- Classifica os pedidos como:
  - Entregue no prazo
  - Entregue com atraso
  - Atrasado (não entregue e prazo já passou)
- Gera um relatório final com os status de cada entrega

## 📁 Estrutura esperada do arquivo `pedidos.xlsx`

| pedido_id | cliente | data_pedido | data_entrega_prevista | data_entregue |
|-----------|---------|-------------|------------------------|----------------|
| 1001      | Ana     | 2024-05-01  | 2024-05-05             | 2024-05-06     |
| ...       | ...     | ...         | ...                    | ...            |

## ✅ Como usar

1. Coloque o arquivo `pedidos.xlsx` na mesma pasta do script
2. Instale as dependências:

```
pip install -r requirements.txt
```

3. Execute o script principal:

```
python main.py
```

4. O arquivo `relatorio_entregas.xlsx` será gerado com os resultados

---

Criado por Davi Teixeira 🚀