from bs4 import BeautifulSoup
import requests
import csv
from time import sleep

# Procedimentos para acessar o site
headers = {
'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
}
s = requests.Session()
s.headers = headers

#Tecnica avancada para pegar varias paginas do iCarro em especifico
preSite = "https://www.icarros.com.br/ache/listaanuncios.jsp?bid=1&app=20&sop=nta_17|44|51.1_-ver_14504|15212|17602|22716|26354|27486|28798.1_-kmm_1.1_-mar_5.1_-mod_2428.1_-esc_4.1_-sta_1.1_&pas=1&pag="
posSite = "&lis=0&ord=16&ope=addFiltro&filtro=ami_amf&vfiltro=2013_2016"
def paginaSite(pre, pos, pagina):
    return pre+str(pagina)+pos


def main():
        media = []
        carros = []

        for k in range(1,20):
            #Procedimento avancado para pegas varias paginas
            site = paginaSite(preSite,posSite, k)
            #Pegando as informacoes de soup, soup seria parser de html, carras dados os dados gerais do carro
            req = s.get(site)
            soup = BeautifulSoup(req.text, 'html.parser')
            carros_dados = soup.find_all("div", class_="anuncio_container false")
            carros_precos = soup.find_all("h3", class_="direita preco_anuncio")


            #laco vai achar todas informacoes relevantes do carro
            for i,carro in enumerate(carros_precos):
                    try:
                        preco_info = carro.string.split()
                        preco = float(preco_info[1].replace(".","").replace(",", "."))
                        ano = int((carros_dados[i].find("li", class_="primeiro")) . text.split()[-1])
                        km = (carros_dados[i].find("li", class_="usado").text.split()[1])
                        km = float(km.replace(".", ""))
                        link = carros_dados[i].find("a").get("href")
                    except: #Algumas vezes o cara escreve algo errado em algum lugar, precisa disso
                        continue
                    carros.append((preco, ano, km, link))
            sleep(1)    #Precisa de um delay, senao o site acha que to atacando ele
        
        #Laco para escrever csv
        i = 2
        j = 1
        with open('iCarros.csv', 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for carro in carros:
                preco, ano, km,link = carro
                writer.writerow([int(preco),ano,int(km), "https://www.icarros.com.br" + link])
                i+=1
                j=1

        print("Achei o preco de {} carros!".format(len(carros)))
        # print("R$: " +  str(median(media)))

if __name__ == '__main__':
    main()

