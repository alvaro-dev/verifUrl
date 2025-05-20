import requests
from bs4 import BeautifulSoup

#url
url = "https://www.iban.com/currency-codes"

#armazena todos os paises e moedas (dicts)
todos_paises = []

#request + soup
r = requests.get(url)
html_doc = r.text
soup = BeautifulSoup(html_doc, 'html.parser')

#filtrar tabela e linhas
tabela = soup.find("tbody")
linhas = tabela.find_all("tr")[1:]


todos_paises = []

#loop em cada linha armazenando os paises no dicts
for linha in linhas:
	itens = linha.find_all("td")
	#desconsiderar moedas no universal currency
	if itens[1].text != "No universal currency":
		pais = {
			"pais": itens[0].text,
			"codigo": itens[2].text
		}
		todos_paises.append(pais)

print(f"<<<<<<<<<< Digite um numero entre 0 e {len(todos_paises)-1} | Digite um numero menor que zero para sair >>>>>>>>>>")
print("BEM VINDO AO NOSSO CONSULTOR DE MOEDA! SELECIONE UMA OPCAO DO MENU!")

for numera, pais in enumerate(todos_paises):
	print(f"## {numera} - {pais['pais']}")

def menu():
	try:
		escolha = int(input("Qual numero? >>"))
		if  escolha > len(todos_paises)-1:
			print(f"Numero maior que a escolha de paises! Digite um número entre 0 e {len(todos_paises)-1}!!")
			menu()
		elif escolha >= 0:
			resultado = todos_paises[escolha]
			print(f"Você escolheu {resultado['pais']} e a moeda é {resultado['codigo']}")
			menu()
		else:
			print("programa encerrado!!!")
	except:
		print("Numero invalido!! Digite um numero valido!!!")
		menu()


menu()
