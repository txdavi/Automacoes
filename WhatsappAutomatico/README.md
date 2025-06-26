# 🤖 WhatsApp Bot com Selenium

Este é um projeto de automação para responder mensagens no **WhatsApp Web** utilizando o **Selenium WebDriver** com Python. O bot detecta automaticamente novas mensagens não lidas e envia respostas automáticas com base em palavras-chave predefinidas. Ideal para pequenas empresas, atendimento básico ou testes com automações.

---

## 📌 Funcionalidades

- Acessa o WhatsApp Web automaticamente.
- Detecta contatos com mensagens **não lidas**.
- Abre a conversa e **verifica apenas as mensagens recebidas no dia atual**.
- Busca por palavras-chave nas mensagens de hoje e responde com uma mensagem adequada.
- **Evita responder repetidamente a mesma palavra-chave para o mesmo contato.**

---

## ⚙️ Tecnologias utilizadas

- Python 3.10+
- Selenium
- WebDriver Manager

---

## ✅ Pré-requisitos

Antes de rodar o projeto, você precisa:

- Ter o Python instalado.
- Instalar as dependências com o comando:

```bash
pip install -r requirements.txt
```

Conteúdo do `requirements.txt`:

```
selenium
webdriver-manager
```

---

## 🚀 Como usar

1. Execute o script principal:

```bash
python whatsapp_bot.py
```

2. Ao rodar o script, o navegador abrirá o **WhatsApp Web**. Escaneie o QR Code com seu celular.

3. O bot começará a monitorar as mensagens não lidas automaticamente.

---

## ✉️ Exemplo de palavras-chave e respostas

Você pode modificar ou expandir o dicionário `respostas` conforme necessário:

```python
respostas = {
    "Oi": "Olá! Como posso te ajudar?",
    "horário": "Nosso horário de atendimento é das 8h às 18h, de segunda a sexta.",
    "preço": "Os preços variam. Qual produto você gostaria de saber?"
}
```

---

## 🔒 Observações de segurança

- O bot foi projetado para responder de forma **simples, realista e espaçada**, simulando o comportamento humano.
- Recomenda-se **não usar** esse bot em grande escala para evitar **bloqueio da conta pelo WhatsApp**.
- **Use apenas com contas que você controla** e para fins educacionais, de teste ou atendimento controlado.

---

## 👨‍💻 Autor

Feito por [Seu Nome] — projeto pessoal com fins de estudo, automação e aprimoramento em Python e Selenium.

---

## 📄 Licença

Este projeto está sob a licença MIT — fique à vontade para utilizar, modificar e compartilhar, desde que com os devidos créditos.
