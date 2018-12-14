import requests
import re
from bs4 import BeautifulSoup


link = 'http://www.banksy.co.uk/'
out = 'out.asp'
r = r"src='(.+?)'"

page = requests.get(link + out)
page.encoding = 'utf-8'
if page.status_code == 200:
	soup = BeautifulSoup(page.text, 'html.parser')
	scripts = soup.find_all('script')
	matches = re.findall(r, scripts[1].get_text())
	for i in range(len(matches)):
		img = requests.get(link + matches[i])
		with open(str(i) + '.jpg', 'wb') as f:
			f.write(img.content)
			print(matches[i])
