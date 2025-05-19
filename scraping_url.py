import requests
from bs4 import BeautifulSoup

#url + request
url_vagas = "https://www.vagas.com.br/vagas-de-python"
r_vagas = requests.get(url_vagas)

#salva o html no html_vagas
html_vagas = r_vagas.text

#faz a sopa
soup = BeautifulSoup(html_vagas, 'html.parser')

cards = soup.find_all('li', class_="vaga odd")

jobs = []

for card in cards:
	job = {
		'title': card.find('a').get('title'),
		'company': card.find('span', class_="emprVaga").get_text(),
		'nivel': card.find('span', class_="nivelVaga").string,
		'how_old': card.find('span', class_="data-publicacao").get_text(),
		'link': f"https://www.vagas.com.br{card.find('a').get('href')}"
	}
	jobs.append(job)

print(jobs)
