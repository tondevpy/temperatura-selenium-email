import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import smtplib
from email.message import EmailMessage

# Função para obter o driver
def obterDriver():
    chrome_options = uc.ChromeOptions()

    prefs = {
        "profile.default_content_setting_values.notifications": 2,  # Bloquear notificações
        "profile.default_content_setting_values.geolocation": 2,    # Bloquear localização
        "profile.default_content_setting_values.media_stream": 2    # Bloquear microfone e câmera
    }
    chrome_options.add_experimental_option("prefs", prefs)

    driver = uc.Chrome(options=chrome_options)

    url = 'https://www.tempo.com/santana-de-parnaiba.htm'
    driver.get(url)

    return driver

# Função para extrair dados
def extrair_dados():
    driver = obterDriver()
    lista = []
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, 'title-h1'))
        )
    
        # Coletar dados
        titulo = driver.find_element(By.CLASS_NAME, 'title-h1').text
        temperatura = driver.find_element(By.CLASS_NAME, 'dato-temperatura').text
        condicao = driver.find_element(By.CLASS_NAME, 'descripcion').text
        sensacao = driver.find_element(By.CLASS_NAME, 'txt-strng').text
        
        # Salvar em um dicionário
        atual = {
            'titulo': titulo,
            'temperatura': temperatura,
            'condicao': condicao,
            'sensacao': sensacao
        }

        lista.append(atual)
    
    except Exception as e:
        print(f"Erro ao extrair dados: {e}")
        return False
    
    finally:
        print('Finalizado')
        driver.quit()

    return lista[0]

dados = extrair_dados()

def enviar_email(dados):
    # Configuração de login de email
    EMAIL_ADDRESS = 'insira seu email aqui'
    EMAIL_PASSWORD = 'insira sua senha aqui' #senha smtp

    # Criação da mensagem de email
    mail = EmailMessage()
    mail['Subject'] = 'Atualização Climática'
    mail['From'] = EMAIL_ADDRESS
    mail['To'] = 'evertonmacieira@icloud.com'

    mensagem = '''
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Dados do Clima</title>
        <style>
        body {{
            font-family: Arial, sans-serif;
            background-color: #f0f8ff;
            color: #333;
            text-align: center;
            margin: 0;
            padding: 0;
        }}

        .container {{
            margin: 20px auto;
            padding: 20px;
            max-width: 400px;
            background-color: #fff;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            border-radius: 10px;
        }}

        h1, h2 {{
            color: #0077b6;
        }}

        p {{
            font-size: 1.1em;
        }}

        a {{
            color: #0077b6;
            text-decoration: none;
            font-weight: bold;
        }}

        a:hover {{
            text-decoration: underline;
        }}
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🌤️ Condições Climáticas</h1>
            <p><strong>Título:</strong> ☀️ {titulo}</p>
            <p><strong>Temperatura:</strong> 🌡️ {temperatura}</p>
            <p><strong>Condição:</strong> ⛅ {condicao}</p>
            <p><strong>Sensação Térmica:</strong> 🌬️ {sensacao}</p>

            <h2>📧 Entre em contato</h2>
            <p>Para mais informações, envie um email para: <a href="mailto:tondevpy@gmail.com">tondevpy@gmail.com</a></p>
        </div>
    </body>
    </html>
    '''.format(
        titulo=dados['titulo'],
        temperatura=dados['temperatura'],
        condicao=dados['condicao'],
        sensacao=dados['sensacao']
    )

    mail.set_content(mensagem, subtype='html')

    # Enviar o email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as email:
        email.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        email.send_message(mail)

enviar_email(dados)