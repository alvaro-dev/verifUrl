import requests
from bs4 import BeautifulSoup

url_vagas = "https://www.vagas.com.br/vagas-de-python"
r_vagas = requests.get(url_vagas)
html_vagas = r_vagas.text

if r_vagas.status_code == 200:
	print("vagas => ok")
	soup = BeautifulSoup(html_vagas, 'html.parser')
	print(soup.prettify())
	print(soup.title)
	links = soup.find_all('a')
	print(lista_a[0])
	for link in links:
		print(link.get('href'))
	print(soup.find('p').text)
	title = soup.find(id="wrapper-pesquisas")
	print(title)
	title_text = title.get('class')
	print(title_text)
else:
	print(r_vagas.status_code)
