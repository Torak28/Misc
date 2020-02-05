import requests
import re
from bs4 import BeautifulSoup
import os


link = 'https://www.kinonh.pl/artykul.do?id=2371'
r = r'href="(.+?)"'
base = 'https://www.kinonh.pl/'

page = requests.get(link)
page.encoding = 'utf-8'
if page.status_code == 200:
	soup = BeautifulSoup(page.text, 'html.parser')
	scripts = soup.find_all("a", {"class": "audio"})
	for script in scripts:
		matches = re.findall(r, str(script))
		for i in range(len(matches)):
			link = str(matches[i]).replace(' ', '%20', 3)
			cmd = 'wget ' + base + link
			os.system(cmd)

# 13 wykładów