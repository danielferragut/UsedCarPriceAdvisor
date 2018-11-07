from bs4 import BeautifulSoup
import requests
from numpy import median
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from time import sleep


# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by nam    e and open the first sheet
# Make sure you use t   he right name here.
sheet = client.open("iCarros_info").sheet1

# Procedimento para acessar o site
headers = {
'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36',
}
s = requests.Session()
s.headers = headers
preSite = "https://www.icarros.com.br/ache/listaanuncios.jsp?bid=1&app=20&sop=nta_17|44|51.1_-ver_14504|15212|17602|22716|26354|27486|28798.1_-kmm_1.1_-mar_5.1_-mod_2428.1_-esc_4.1_-sta_1.1_&pas=1&pag="
posSite = "&lis=0&ord=16&ope=addFiltro&filtro=ami_amf&vfiltro=2013_2016"


def paginaSite(pre, pos, pagina):
    return pre+str(pagina)+pos


def main():
        media = []
        carros = []

        #Pegando as informacoes de soup
        for k in range(1,4):
            site = paginaSite(preSite,posSite, k)
            req = s.get(site)
            soup = BeautifulSoup(req.text, 'html.parser')
            carros_dados = soup.find_all("div", class_="dados_veiculo")
            carros_precos = soup.find_all("h3", class_="direita preco_anuncio")


            for i,carro in enumerate(carros_precos):
                    preco_info = carro.string.split()
                    preco = float(preco_info[1].replace(".","").replace(",", "."))
                    ano = int((carros_dados[i].find("li", class_="primeiro")) . text.split()[1][:-1])
                    km = (carros_dados[i].find("li", class_="usado").text.split()[1])
                    if km == "N/D":
                        continue
                    km = float(km.replace(".", ""))
                    carros.append((preco, ano, km))
            sleep(1)
        i = 2
        j = 1
        for carro in carros:
            preco, ano, km = carro
            sheet.update_cell(i, j, preco)
            sleep(2)
            sheet.update_cell(i, j+1, ano)
            sleep(2)
            sheet.update_cell(i, j+2, km)
            sleep(2)
            i+=1
            j=1

        print("Achei o preco de {} carros!".format(len(carros)))
        # print("R$: " +  str(median(media)))

if __name__ == '__main__':
    main()

