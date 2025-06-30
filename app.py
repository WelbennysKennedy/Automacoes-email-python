# Importar biblioteca
import smtplib
from email.message import EmailMessage
import mimetypes

# Defenir os dados de envio
remetente = 'seu email aqui'
destinatario = 'a pessoa que receberá o email aqui'
assunto = 'Teste de envio de email'
mensagem = """
Olá, este é um teste de envio de email utilizando Python.
Espero que esteja funcionando corretamente!   
"""
senha = 'miji mtns pdpr uxjk'
anexo = 'html-css-basico-exercicio-3-paragrafos-coloridos.pdf'

# Criar Email Message
msg = EmailMessage()
msg['From'] = assunto
msg['To'] = remetente
msg['Subject'] = destinatario
msg.set_content(mensagem)

# anexar o arquivo
manme_type, _ = mimetypes.guess_type(anexo)
mime_type, mime_subtype = manme_type.split('/')
with open(anexo, 'rb') as arquivo:
    msg.add_attachment(arquivo.read(), maintype=mime_type, subtype=mime_subtype, filename=anexo)

# Realizar o envio do email
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as email:
    email.login(remetente, senha)
    email.send_message(msg)


    print('Email enviado com sucesso!')