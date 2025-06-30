# 📧 Email Table Extractor

**Email Table Extractor** é um script Python que conecta-se à sua conta de e-mail via IMAP, localiza o e-mail mais recente de um remetente específico, extrai qualquer tabela HTML contida no corpo da mensagem e exporta os dados para um arquivo Excel (`.xlsx`).

---

## ✨ Principais Funcionalidades

✅ Login seguro via IMAP com variáveis de ambiente  
✅ Leitura e decodificação de conteúdo HTML do e-mail  
✅ Detecção automática de codificação de caracteres com `chardet`  
✅ Extração de tabelas HTML com `BeautifulSoup` + `pandas`  
✅ Exportação automática para Excel (`tabela_email.xlsx`)  

---

## 📂 Estrutura do Projeto

email-table-extractor/
├── main.py # Script principal
├── .env # Variáveis de ambiente (não subir para o GitHub)
├── requirements.txt # Lista de dependências
└── tabela_email.xlsx # Arquivo Excel gerado com os dados da tabela (criado automaticamente)

---

## ⚙️ Configuração e Execução

### 1. Instale as dependências

pip install -r requirements.txt
Ou instale diretamente:

pip install pandas beautifulsoup4 python-dotenv chardet lxml openpyxl

2. Crie o arquivo .env

Adicione suas credenciais:

EMAIL_USER=seu_email@gmail.com

EMAIL_PASS=sua_senha_de_app

⚠️ Importante: Para contas Gmail, ative a verificação em duas etapas e gere uma senha de app:

Como gerar senha de app no Gmail - > link: https://support.google.com/mail/answer/185833

🧠 Como o Script Funciona

Carrega as credenciais do .env

Conecta ao servidor IMAP (imap.gmail.com)

Acessa a caixa de entrada (INBOX)

Busca mensagens de um remetente específico

Seleciona o e-mail mais recente

Extrai e decodifica o conteúdo HTML

Localiza a <table> dentro do HTML

Converte a tabela em um DataFrame com o pandas

Exporta os dados para o arquivo tabela_email.xlsx

🛠️ Personalização

No início do script (main.py), você pode alterar os seguintes parâmetros:


IMAP_SERVER = 'imap.gmail.com'       # Servidor IMAP do provedor

MAILBOX = 'INBOX'                    # Caixa onde será feita a busca

REMETENTE = 'remetente@exemplo.com'  # E-mail do remetente a ser filtrado

📤 Exemplo de Saída

Após execução bem-sucedida, será gerado o arquivo:

📄 tabela_email.xlsx

Contendo a tabela extraída diretamente do e-mail, pronta para análise ou processamento.

📌 Notas Importantes

O script extrai apenas a primeira tabela encontrada no corpo HTML do e-mail.

Não lê e-mails com anexos, apenas conteúdo HTML com <table>.

O código utiliza chardet para lidar com e-mails que não usam codificação UTF-8.

🤝 Contribuições

Sinta-se à vontade para abrir issues, sugerir melhorias ou enviar um Pull Request.
Toda contribuição é bem-vinda!

📜 Licença

Distribuído sob a Licença MIT. Veja LICENSE para mais informações.

