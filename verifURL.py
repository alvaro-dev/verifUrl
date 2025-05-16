import requests

def menu():
	escolha = str(input("Verifica mais um site? (s/n)")).lower()
	if escolha == "s":
		main()
	elif escolha == "n":
		print("Programa encerrado")
		return
	else:
		print("Opção inválida")
		menu()

def main():
	#print de boas vindas
	print("Insira o(s) site(s) para verificar: (separado por vírgula)")
	#pega url(input)
	urls = str(input()).lower().split(",")
	#percorre cada url
	for url in urls:
		url = url.strip()
		if "." not in url:
			print(url, "url inválida")
		else:
			if "http" not in url:
				url = f"http://{url}"
			try:
				requisicao = requests.get(url)
				if requisicao.status_code == 200:
					print(url,"site online")
				else:
					print(url, "site offline")
			except:
				print(url, "erro")
	menu()

#init
main()
