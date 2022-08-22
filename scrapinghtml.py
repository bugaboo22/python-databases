import urllib.request
import urllib.parse
import urllib.error
import json
from bs4 import BeautifulSoup

url = 'http://py4e-data.dr-chuck.net/comments_1595292.json'
print('Retrieving', url)

uh = urllib.request.urlopen(url)
data = uh.read()
info = json.loads(data.decode())

print('User count:', len(info))
comments_dic = info['comments']

total = 0

for item in comments_dic:
    total = total + int(item['count'])
print(total)