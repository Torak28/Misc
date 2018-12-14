import requests
from datetime import datetime
from bs4 import BeautifulSoup
from prettytable import PrettyTable
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


def get_data():
	all_players = []

	link = 'http://www.rotoworld.com/teams/injuries/nba/all/'
	page = requests.get(link)
	page.encoding = 'utf-8'
	if page.status_code == 200:
		soup = BeautifulSoup(page.text, 'html.parser')
		team_tables = soup.find_all('div', attrs={'class': 'pb'})
		for team in team_tables:
			team_name = team.find('div', attrs={'class': 'headline'}).find('div', attrs={'class': 'player'}).text
			players = team.find_all('tr')
			for player in players:
				if player.find('a', href=True) is not None:
					name = player.find('a', href=True).text
					player_data = player.find_all('td')
					position = player_data[2].text
					status = player_data[3].text
					date = str(datetime.strptime(player_data[4].text + ' 2018', '%b %d %Y').date())
					injury = player_data[5].text
					returns = player_data[6].text
					one_player = dict(name=name, team=team_name, position=position, status=status, date=date, injury=injury, returns=returns)
					all_players.append(one_player)
	return all_players


def sort_data(data):
	sorted_players = sorted(data, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%d'))
	return sorted_players


def print_data(data):
	table = PrettyTable(['Name', 'Team', 'Position', 'Status', 'Date', 'Injury', 'Returns'])
	for player in data:
		table.add_row([player['name'], player['team'], player['position'], player['status'], player['date'], player['injury'], player['returns']])
	return table

out = print_data(sort_data(get_data()))
print(out.get_string())

img = Image.new('RGB', (765, 1500))
draw = ImageDraw.Draw(img)
font = ImageFont.load_default()
draw.text((10, 10), out.get_string(), fill=(255, 255, 255), font=font)

img.save('out.png')
