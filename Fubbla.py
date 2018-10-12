#!/usr/bin/python3
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup

#Email transfer
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
    
print(soup.prettify())

password = open('credentials.txt', 'r').read()

print(password)

S = smtplib.SMTP('ssrs.reachmail.net',2525)
S.login('hauke.diers@outlook.com', password)

