# importando bibliotecas
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# relacionando a conta para envio dos emails
your_email = ""
your_password = ""

# estabelecendo uma conexao smtp do provedor de email
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(your_email, your_password)

# lendo arquivo com dados de emails e nomess
email_list = pd.read_excel('/**/**')

# recebendo os nomes e emails do arquivo
names = email_list['']
emails = email_list[]

# iteração para receber dados e enviar emails
for i in range(len(emails)):
    # gravando todos nomes e emails do arquivo lido pelos pandas
    name = names[i]
    email = emails[i]


    # criando mensagem para emails
    message = MIMEMultipart()
    message['From'] = ''
    message['To'] = email
    message['Subject'] = ""

    # Mensagem no corpo do email
    body = ("")
    message.attach(MIMEText(body, 'plain'))

    # Anexando arquivo
    with open('/**/**', 'rb') as attachment:
        part = MIMEApplication(attachment.read())
        part.add_header('Content-Disposition', 'attachment', filename='file.pdf')
        message.attach(part)

    # enviando email
    server.sendmail(your_email, email, message.as_string())

# fechando conexao com servidor smtp
server.quit()
