import requests
from requests.auth import HTTPDigestAuth
from bs4 import BeautifulSoup
url = 'http://gcdb-vs01.cc.lut.fi/dashboard/db/realtime-production?refresh=5s&orgId=4'
r = requests.get(url, auth = HTTPDigestAuth('Greencampus', 'Ohcaghoh7Wohx1xoo0phoos'))
print(r.text)

