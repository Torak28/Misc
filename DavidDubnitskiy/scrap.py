import requests
from bs4 import BeautifulSoup

requests.adapters.DEFAULT_RETRIES = 5

# rewrite using https://pypi.org/project/requests-html/

base = 'https://500px.com'
some_id = '?ctx_page=1&from=user&user_id=5461522'

with open('input', 'r') as f:
	soup = BeautifulSoup(f, 'html.parser')
	imgs = soup.find_all('img')
	imgs = [imgs[4]]
	for i in range(len(imgs)):
		img = imgs[i]['src']
		if '/photo/' in img:
			new_url = base + imgs[i].parent['href'] + some_id
			# print(new_url)
			page = requests.get(new_url)
			if page.status_code != 200:
				print(f'BŁĄÐ: {new_url}')
			else:
				big_imgs = soup.find_all('div', class_='Elements__PhotoImageSafariFixWrapper')
				print(len(big_imgs))
				print(page.text)
			# print(page.status_code)
			# with open(str(i) + '.jpg', 'wb') as ff:
			# 	ff.write(requests.get(img).content)
			# 	print(str(i))

# Sporo new_url nie działa

#god: https://500px.com/photo/1001044381/Sophie-and-music-2-by-David-Dubnitskiy?ctx_page=1&from=user&user_id=5461522
#bad: https://500px.com/photo/1001044381/Sophie-and-music-2-by-David-Dubnitskiy?ctx_page=1&from=user&user_id=5461522