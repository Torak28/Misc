import requests
from bs4 import BeautifulSoup


links = ['http://www.birkajazz.com/archive/blueNote10inch.htm', 'http://www.birkajazz.com/archive/blueNote1500.htm', 'http://www.birkajazz.com/archive/blueNote4000.htm']

for j in range(len(links)):
	page = requests.get(links[j])
	if page.status_code == 200:
		soup = BeautifulSoup(page.text, 'html.parser')
		imgs = soup.find_all('image')
		for i in range(len(imgs)):
			img = requests.get('http://www.birkajazz.com/' + imgs[i]['src'][3:])
			with open(str(j) + '-' + str(i) + '.jpg', 'wb') as f:
				f.write(img.content)
				print(imgs[i]['src'][3:])
