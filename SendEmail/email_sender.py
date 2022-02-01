import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path


html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'َAlbertPedar'
email['to'] = 'mohammaddavoodi107@gmail.com'
email['subject'] = 'You won 1M dollars!'
email.set_content(html.substitute({'name': 'Mohammad'}), 'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('examplmailsender@gmail.com', 'py12512prj')
    smtp.send_message(email)

    print('all good Boss!')
