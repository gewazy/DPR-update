import smtplib
from email.message import EmailMessage

import init
import password

subject = f'{init.GRUPA} Raport Geodezyjny'
sender = f"{init.GRUPA}surveyor@geofizyka.pl"


wiadomosc = f'''
Dzień dobry,

Raporty geodezyjne  w załączniku.

{input('Jeśli chcesz coś dodać do maila, pisz teraz, jak nie -> ENTER: ')}


Dominik Jurkowski
Grupa sejsmiczna {init.GRUPA} '''

# create mail
msg = EmailMessage()

msg['Subject'] = subject
msg['From'] = sender
msg['To'] = init.RECIPIENT
msg.set_content(wiadomosc)

# dodanie załączników
for plik in init.DPR:
    with open(plik, 'rb') as f:
        zalacznik = f.read()
    msg.add_attachment(zalacznik, maintype="application",
                       subtype=plik.split('.')[-1], filename=plik.split('\\')[-1])

smtp_server = smtplib.SMTP("smtp.geofizyka.pl", 587, timeout=120)
smtp_server.ehlo() #setting the ESMTP protocol
smtp_server.starttls() #setting up to TLS connection
smtp_server.login(f'{init.GRUPA.lower()}surveyor', password.PASSWORD)  # user and pass
smtp_server.send_message(msg)
print('Wiadomość została wysłana')
smtp_server.quit()
