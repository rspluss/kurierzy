from django.shortcuts import render

from bs4 import BeautifulSoup
from requests import get


def home(request):

    url = 'https://www.bankier.pl/inwestowanie/profile/quote.html?symbol=MWIG40'
    page = get(url)
    bs = BeautifulSoup(page.content, 'html.parser')

    index_gpw = {}
    number = 0
    for offer in bs.find_all('tr'):
        name = offer.find('td', class_='colWalor')
        price = offer.find('td', class_='colKurs')
        if name == None:
            continue
        if price == None:
            continue
        name_index = name.get_text().strip()
        price_index = price.get_text().strip()

        index_gpw[name_index] = price_index
        number += 1
        if number == 5:
            break
    print(index_gpw)

    context = {'index_gpw': index_gpw}
    return render(request, "gpw/index.html", context)
