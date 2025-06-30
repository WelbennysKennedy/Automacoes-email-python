# 📧 Envio de E-mails com Python (com Anexo)

Este projeto demonstra como automatizar o envio de e-mails utilizando Python, incluindo o envio de **anexos** (como PDFs) de forma simples e segura via `SMTP_SSL`.

## 🚀 Tecnologias utilizadas

- Python 3.x
- `smtplib`
- `email.message.EmailMessage`
- `mimetypes`

## 🧠 Como funciona

O script executa os seguintes passos:

1. Define os dados do remetente, destinatário, assunto, corpo do e-mail e o caminho do arquivo a ser anexado.
2. Cria a mensagem com `EmailMessage()`.
3. Identifica automaticamente o tipo do anexo com `mimetypes`.
4. Anexa o arquivo ao e-mail.
5. Envia o e-mail via servidor SMTP do Gmail, com autenticação segura (`SMTP_SSL`).

## 📄 Exemplo de uso

python
remetente = 'seu_email@gmail.com'
destinatario = 'destinatario@gmail.com'
senha = 'sua_senha_app_google'
anexo = 'documento.pdf'


⚠️ Importante: Para usar com o Gmail, é necessário gerar uma senha de app no painel de segurança da sua conta Google (não use sua senha principal).

🛡️ Segurança
Nunca compartilhe sua senha real. Use variáveis de ambiente ou arquivos .env para manter as credenciais protegidas.

📬 Resultado
E-mail enviado com sucesso.

Anexo incluso no corpo do e-mail.

Automatização ideal para envio de relatórios, alertas ou notificações.

📌 Licença
Este projeto está sob a licença MIT. Sinta-se livre para usar, modificar e compartilhar.

Feito com 💻 por [Welbenes Kenedy]


Thanks!!!
