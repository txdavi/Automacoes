import imaplib # Ajuda a entrar no e-mail e ler mensagens
import email # Ajuda a entender as mensagens de e-mail
from email.header import decode_header # Decodifica o título do e-mail (caso tenha símbolos estranhos).
from bs4 import BeautifulSoup # Ajuda a "ler" páginas da web (ou e-mails em HTML).
from io import StringIO # Ajuda a transformar textos em arquivos temporários.
import pandas as pd # Ajuda a criar tabelas e salvar arquivos.
import os # Permite pegar informações do sistema, como a senha do e-mail.
from dotenv import load_dotenv
import chardet # biblioteca para detectar a codificação

#Carregar variáveis de ambiente
load_dotenv()

# Pegando as informações do e-mail

EMAIL_USER = os.getenv('EMAIL_USER') # Pega informações de usuário no arquivo .env
EMAIL_PASS = os.getenv('EMAIL_PASS') # Pega informações de senha no arquivo .env

#Ajuste do seu provedor

IMAP_SERVER = 'imap.gmail.com' # O endereço do e-mail que estamos acessando (no caso, Gmail).
MAILBOX = 'INBOX' # A caixa onde estão os e-mails (normalmente "INBOX").
REMETENTE = 'EMAIL DO REMETENTE' # O e-mail da pessoa que enviou a mensagem que queremos ler.

# Entrando no e-mail

mail = imaplib.IMAP4_SSL(IMAP_SERVER) # Conecta ao servidor de e-mail.
mail.login(EMAIL_USER, EMAIL_PASS) # Faz o login.
mail.select(MAILBOX) # Escolhe a caixa de entrada para procurar mensagens.

# Procurando um e-mail do remetente certo

status, messages = mail.search(None, f'FROM "{REMETENTE}"') # Pede ao e-mail para encontrar mensagens desse remetente.
email_ids = messages[0].split() # Pega os códigos dos e-mails encontrados.

# Pegando o e-mail mais recente

if email_ids:
    latest_email_id = email_ids[-1] # Pega o último e-mail recebido.
    status, data = mail.fetch(latest_email_id, '(RFC822)') # Baixa esse e-mail.
    raw_email = data[0][1] # Guarda o conteúdo do e-mail.

    # Entendendo o e-mail

    msg = email.message_from_bytes(raw_email) # Aqui estamos abrindo o e-mail e pegando o que tem dentro.
    if msg.is_multipart(): # Vê se o e-mail tem várias partes (texto, imagens, etc.).
        for part in msg.walk(): # Percorre cada parte do e-mail.
            if part.get_content_type() == 'text/html': # Procura a parte que contém um site ou tabela.
                html_content = part.get_payload(decode=True) # Lê o conteúdo em bytes.

                # Detectando a codificação correta do conteúdo
                detected_encoding = chardet.detect(html_content)['encoding']
                html_content = html_content.decode(detected_encoding, errors='replace') # Decodifica com a codificação detectada
                break
    else:
        html_content = msg.get_payload(decode=True) # Se não for multipart, só decodifica o conteúdo
        # Detectando a codificação correta do conteúdo
        detected_encoding = chardet.detect(html_content)['encoding']
        html_content = html_content.decode(detected_encoding, errors='replace')

    # Encontrando a tabela dentro do e-mail
    
    soup = BeautifulSoup(html_content, 'html.parser') # Transforma o e-mail em um formato mais fácil de ler.
    table = soup.find('table') # Procura uma tabela no e-mail.

    if table:
        df = pd.read_html(StringIO(str(table)))[0] # Converte essa tabela para um formato de planilha.

        #Salvar no Excel     
        df.to_excel('tabela_email.xlsx', index=False) # Cria um arquivo chamado "tabela_email.xlsx".
        print("Tabela salva com sucesso!")

    else:
        print("Nenhuma tabela encontrada no e-mail")

else:
    print("Nenhum e-mail encontrado.")
