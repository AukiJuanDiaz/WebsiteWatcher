#!/usr/bin/python3
import urllib.request
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup

top_level_url = "https://www.service.tuhh.de/qissos/rds?state=user&type=0"

# create a password manager
password_mgr = urllib.request.HTTPPasswordMgrWithDefaultRealm()

# Add the username and password.
# If we knew the realm, we could use it instead of None.
username, password = open('credentials_TUHH_SOS.txt', 'r').read().splitlines()
print("usertname:",username)
print("password:",password)
print("a","b")
password_mgr.add_password(None, top_level_url, username, password)

handler = urllib.request.HTTPBasicAuthHandler(password_mgr)

# create "opener" (OpenerDirector instance)
opener = urllib.request.build_opener(handler)

try:
    # use the opener to fetch a URL
    response = opener.open("https://www.service.tuhh.de/qissos/rds?state=user&type=0&topitem=&breadCrumbSource=&topitem=functions")
except HTTPError as e:
    print('Error code: ',e.code)
except URLError as e:
    print('Reason: ',e.reason)
else:
    print('good!')
    soup = BeautifulSoup(response, 'html.parser')
    print(soup.prettify())
    

