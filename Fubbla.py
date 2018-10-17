#!/usr/bin/python3
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup

# Email transfer
import smtplib
from email.mime.text import MIMEText

req = Request("https://www.ikea.com/de/de/catalog/products/20325687/")
try:
    response = urlopen(req)
except HTTPError as e:
    print('Error code: ',e.code)
except URLError as e:
    print('Reason: ',e.reason)
else:
    print('good!')
    soup = BeautifulSoup(response, 'html.parser')
    
# print(soup.find("div", {"id":"popupAddToCart20325687_"}))
input_btn = soup.find("input", {"name":"add", "value":"In den Warenkorb"})          
print(input_btn['type'])

# Prepare the Email-Server
password = open('credentials_Email.txt', 'r').read()
s = smtplib.SMTP('ssrs.reachmail.net',25)
s.login('hauke.diers@outlook.com', password)

# Prepare the Email-Message
with open('Hello_Email.txt') as fp:
    msg = MIMEText(fp.read())

msg['Subject']= 'Raspberry Pi Email'
msg['From'] = 'Hauke.diers@outlook.com'
msg['To'] = 'Hauke.diers@outlook.com'

# Comment in the Email to send
# s.send_message(msg)
s.quit()

