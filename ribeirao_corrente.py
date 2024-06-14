import requests
from bs4 import BeautifulSoup
from tinydb import TinyDB, Query

def acessar_pagina(url):
    pagina = requests.get(url)
    bs = BeautifulSoup(pagina.text, "html.parser")
    return bs

def extrair_infos(url_base):
    pagina=acessar_pagina(url_base)
    print(pagina)
    # numero da edição, data, link do pdf, ano
    # https://api-do.eddydata.com/diario-oficial/api/v1/publicacoes/downloadFile/DO-00610-2024.pdf
    # https://api-do.eddydata.com/diario-oficial/api/v1/publicacoes/filtro-pdf-data?data1=2023-01-01&data2=2023-03-31&agendamento=2024-06-14&cidade=1&page=0&linesPerPage=100&orderBy=dataPublicacao&direction=DESC
def main():
    url_base="https://sistemas.eddydata.com/pmribeirao-corrente/diario-oficial/#/doe/ribeiraocorrente"
    extrair_infos(url_base)

if __name__ == "__main__":
    main()
