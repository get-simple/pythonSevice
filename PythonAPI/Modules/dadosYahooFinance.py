from urllib.request import urlopen
from bs4 import BeautifulSoup


def UltimoPreco(ativo):
    url = f'https://finance.yahoo.com/quote/{ativo}.SA?p={ativo}.SA'

    response = urlopen(url)
    html = response.read()

    soup = BeautifulSoup(html, 'html.parser')

    preco = soup.find(
        'span', {'class': 'Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)'}
    ).get_text()
    print(preco)
    return preco
