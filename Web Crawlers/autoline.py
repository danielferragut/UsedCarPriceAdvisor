from bs4 import BeautifulSoup
import requests
from numpy import median

headers = {
'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
}
s = requests.Session()
s.headers = headers

def main():
        media = []
        # site = "https://www.webmotors.com.br/carros/estoque/chevrolet/onix?qt=36&p=1"
        site = "https://busca.autoline.com.br/comprar/carros/seminovos-usados/todos-os-estados/todas-as-cidades/chevrolet/onix/1.0-joy-8v-flex-4p-manual/todos-os-anos/todas-as-cores/todos-os-precos/?page=1"
        req = s.get(site)
        soup = BeautifulSoup(req.text, 'html.parser')
        carros = soup.find_all("a", class_="nm-price-value")
        extrainfor = soup.find_all("li", class_="nm-extra-info")
        for i in carros:
                k = i.string.split()
                # print("{} {}".format(k[0], k[1]))
                media.append(float(k[1].replace(".","").replace(",", ".")))
        
        print(median(media))

if __name__ == '__main__':
    main()

