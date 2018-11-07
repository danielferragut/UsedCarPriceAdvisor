from bs4 import BeautifulSoup
import requests
from numpy import median
import csv

headers = {
'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
"accept-encoding": "gzip, deflate, br",
}
s = requests.Session()
s.headers = headers
preSite = "https://www.webmotors.com.br/carros-usados/estoque/chevrolet/onix/10-mpfi-lt-8v-flex-4p-manual?tipoveiculo=carros-usados&marca1=chevrolet&modelo1=onix&versao1=1.0%20mpfi%20lt%208v%20flex%204p%20manual&anunciante=ag%C3%AAncias%20de%20publicidade%7Cconcession%C3%A1ria%7Cloja%7Cpessoa%20f%C3%ADsica&estadocidade=estoque&p="
posSite = "&o=1&qt=36"

def paginaSite(pre, pos, pagina):
    return pre+str(pagina)+pos

def main():
	carros = []
	lim = 60
	for w in range(1,lim):
		site = paginaSite(preSite, posSite, w)
		req = s.get(site)
		soup = BeautifulSoup(req.content, 'html.parser')
		info_carros = soup.find_all("div", class_="info-veiculo-detalhe")
		precos_carros = soup.find_all("div", class_="price-novo space-preco")
		j = 0
		print("Estou na página {} de {}...".format(w, lim))
		for i, carro in enumerate(precos_carros):
			try:
				preco =  ((carro.text.split()[1].replace(".", "")))
				ano  = (info_carros[j].text)
				ano = (ano.split()[0].split(sep="/")[1])
				km = (info_carros[j+1].text.split()[0].replace(".", ""))
				j+=3
			except:
				continue
			carros.append((preco, ano, km))
	        #Laco para escrever csv
	a = 2
	j = 1
	with open('webmotors.csv', 'w', newline='') as csvfile:
		writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
		for carro in carros:
			preco, ano, km = carro
			writer.writerow([preco,ano,km])
	print("Achei {} carros!".format(len(carros)))
		
if __name__ == '__main__':
	main()

