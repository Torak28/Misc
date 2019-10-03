import requests
from bs4 import BeautifulSoup

with open('input', 'r') as f:
	soup = BeautifulSoup(f, 'html.parser')
	imgs = soup.find_all('img')
	for i in range(len(imgs)):
		img = imgs[i]['src']
		if '/photo/' in img:
			with open(str(i) +  'jpg', 'wb') as ff:
				ff.write(requests.get(img).content)
				print(str(i))