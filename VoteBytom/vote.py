import requests
from bs4 import BeautifulSoup

bartyla_all, czubak_all, janas_all, michalowski_all, panek_all, wezyk_all, wolosz_all, nope = 0, 0, 0, 0, 0, 0, 0, 0
names, errors = [], []

for i in range(1, 80):
	link = 'https://wybory2018.pkw.gov.pl/pl/geografia/246201/pollstation/' + str(i)
	page = requests.get(link)
	page.encoding = 'utf-8'
	if page.status_code == 200:
		print(link)
		soup = BeautifulSoup(page.text, 'html.parser')
		stat_table = soup.find('table', attrs={'class': 'stat_table'})
		com_name = stat_table.find_all('tr')[0].find_all('td')[1].get_text()
		succes = False
		poll_tables = soup.find_all('table', attrs={'class': 'stat_table stat_table_dt'})
		for tmp in poll_tables:
			all_links = tmp.find_all('a')
			for i in range(len(all_links) - 1):
				if all_links[i].get_text() == 'bartyla damian franciszekBARTYLA Damian Franciszek' and all_links[i + 1].get_text() == 'czubak jan kazimierzCZUBAK Jan Kazimierz':
					poll_table = tmp
					poll_table_results = poll_table.find_all('td', attrs={'class': 'table-number'})
					bartyla_all += int(poll_table_results[0].find('span').next_sibling) if poll_table_results[0].find('span') is not None else 0
					czubak_all += int(poll_table_results[1].find('span').next_sibling) if poll_table_results[1].find('span') is not None else 0
					janas_all += int(poll_table_results[2].find('span').next_sibling) if poll_table_results[2].find('span') is not None else 0
					michalowski_all += int(poll_table_results[3].find('span').next_sibling) if poll_table_results[3].find('span') is not None else 0
					panek_all += int(poll_table_results[4].find('span').next_sibling) if poll_table_results[4].find('span') is not None else 0
					wezyk_all += int(poll_table_results[5].find('span').next_sibling) if poll_table_results[5].find('span') is not None else 0
					wolosz_all += int(poll_table_results[6].find('span').next_sibling) if poll_table_results[6].find('span') is not None else 0
					succes = True
					break
		if succes is False:
			nope += 1
			names.append(com_name)
	else:
		errors.append(link)

sum_all = bartyla_all + czubak_all + janas_all + michalowski_all + panek_all + wezyk_all + wolosz_all

print(f'Nie ma wynikow z {nope} lokali, w tym {names}\n')
print(f'Do tej pory({79 - nope} lokali) wyniki sa nastepujace:\
	\n\tDamian Bartyla: {bartyla_all} ({bartyla_all/sum_all * 100:.2f}%)\
	\n\tJan Czubak: {czubak_all} ({czubak_all/sum_all * 100:.2f}%)\
	\n\tMariusz Janas: {janas_all} ({janas_all/sum_all * 100:.2f}%)\
	\n\tMarek Michałowski: {michalowski_all} ({michalowski_all/sum_all * 100:.2f}%)\
	\n\tAndrzej Panek: {panek_all} ({panek_all/sum_all * 100:.2f}%)\
	\n\tAndrzej Wężyk: {wezyk_all} ({wezyk_all/sum_all * 100:.2f}%)\
	\n\tMariusz Wolosz: {wolosz_all} ({wolosz_all/sum_all * 100:.2f}%)')
print(f'\nNie dzialaly strony: {errors}')
