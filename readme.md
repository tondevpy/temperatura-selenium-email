# Atualização Climática com Selenium e Envio de Email

Este projeto automatiza a extração de dados climáticos de cidades utilizando o Selenium com o `undetected-chromedriver`. Após a coleta dos dados, o script envia um email com as informações extraídas de forma automatizada.

## Funcionalidades

- Coleta de informações climáticas de um site específico.
  - **Título da página**
  - **Temperatura**
  - **Condição climática**
  - **Sensação térmica**
- Envio dos dados coletados por email, utilizando o protocolo SMTP via Gmail.
- Formatação do email em HTML com emojis para tornar a mensagem mais visual.

## Tecnologias Utilizadas

- **Python 3.x**
- **Selenium** com `undetected_chromedriver`
- **SMTP** para envio de emails
- **HTML e CSS** para formatação do corpo do email

## Pré-requisitos

- **Python 3.x** instalado em sua máquina
- Conta de **Gmail** para envio de emails
- Habilitar a funcionalidade de aplicativos menos seguros no Gmail ou gerar uma senha de aplicativo específico para autenticação SMTP.
