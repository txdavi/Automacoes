# Importando todas as ferramentas necessárias
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import datetime

# Inicia o navegador Chrome usando o WebDriver Manager
navegador = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Abre o site do WhatsApp Web
navegador.get("https://web.whatsapp.com")

# Espera até que o painel lateral (com as conversas) apareça, indicando que o WhatsApp carregou
while len(navegador.find_elements(By.ID, 'side')) < 1:
    time.sleep(1)

# Espera adicional para garantir que tudo esteja carregado corretamente
time.sleep(10)

# Define palavras-chave e as respostas automáticas correspondentes
respostas = {
    "oi": "Olá! Como posso te ajudar?",
    "horário": "Nosso horário de atendimento é das 8h às 18h, de segunda a sexta.",
    "preço": "Os preços variam. Qual produto você gostaria de saber?"
}

# Dicionário para guardar quais palavras já foram respondidas para cada contato
respostas_enviadas = {}

# Loop principal: roda para sempre
while True:
    # Encontra todos os contatos com mensagens não lidas
    contatos_nao_lidos = navegador.find_elements(
        By.XPATH, '//span[@aria-label="Não lidas"]/ancestor::div[@role="listitem"]'
    )

    if len(contatos_nao_lidos) > 0:
        # Pega o primeiro contato com mensagem não lida
        contato = contatos_nao_lidos[0]

        # Garante que o contato esteja visível na tela
        navegador.execute_script("arguments[0].scrollIntoView(true);", contato)
        time.sleep(1)
        contato.click()
        time.sleep(3)

        # Lê o nome do contato no topo da conversa
        nome_contato = navegador.find_element(By.XPATH, '//header//span[@dir="auto"]').text

        # Se ainda não tivermos registrado esse contato, criamos uma lista para ele
        if nome_contato not in respostas_enviadas:
            respostas_enviadas[nome_contato] = []

        # Encontra a área da conversa
        container_conversa = navegador.find_element(By.XPATH, '//div[@data-tab="8" and @role="application"]')

        # Pega todas as mensagens da conversa
        mensagens_completas = container_conversa.find_elements(By.CSS_SELECTOR, 'div.copyable-text')

        # Verifica qual é a data de hoje
        hoje = datetime.date.today()
        mensagens_de_hoje = []

        # Filtra as mensagens enviadas HOJE
        for msg in mensagens_completas:
            data_texto = msg.get_attribute('data-pre-plain-text')
            if data_texto:
                try:
                    data = data_texto.split(',')[1].strip().split(']')[0]
                    mes, dia, ano = data.split('/')
                    data_msg = datetime.date(int(ano), int(mes), int(dia))

                    # Se a mensagem é de hoje, adiciona à lista
                    if data_msg == hoje:
                        mensagens_de_hoje.append(msg)
                except Exception as e:
                    print("Erro ao extrair data da mensagem", e)

        print(f"Total de mensagens de hoje: {len(mensagens_de_hoje)}")

        if mensagens_de_hoje:
            print("Última mensagem de hoje:", mensagens_de_hoje[-1].text)
            resposta_final = None
            palavra_detectada = None

            # Para cada mensagem de hoje, verifica se contém uma palavra-chave
            for mensagens in mensagens_de_hoje:
                texto_mensagem = mensagens.text.lower()

                for palavra, resposta in respostas.items():
                    if palavra.lower() in texto_mensagem and palavra not in respostas_enviadas[nome_contato]:
                        resposta_final = resposta
                        palavra_detectada = palavra
                        break
                if resposta_final:
                    break

            # Se encontrou alguma palavra-chave e gerou uma resposta...
            if resposta_final:
                try:
                    # Encontra o campo de digitar mensagem
                    campo_mensagem = navegador.find_element(By.XPATH, '//div[@aria-label="Digite uma mensagem"]')

                    # Clica no campo e digita a resposta
                    ActionChains(navegador).move_to_element(campo_mensagem).click().perform()
                    time.sleep(1)
                    campo_mensagem.send_keys(resposta_final + Keys.ENTER)
                    print(f"Resposta enviada para {nome_contato}: {resposta_final}")

                    # Anota que já respondeu essa palavra para esse contato
                    if palavra_detectada is not None:
                        respostas_enviadas[nome_contato].append(palavra_detectada)

                except Exception as e:
                    print("Erro ao enviar mensagem:", e)
        else:
            print("Nenhuma mensagem de hoje encontrada.")

    else:
        print("Nenhum contato com mensagens não lidas no momento.")
    time.sleep(20)
