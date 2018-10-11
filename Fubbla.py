#!/usr/bin/python3
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup


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