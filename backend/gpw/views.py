from django.shortcuts import render
from .models import Index

from bs4 import BeautifulSoup
from requests import get


def home(request):
    indexes = Index.objects.all()

    for index in indexes:
        print(index.name)
        if index.name == index.name:
            print("tak")

    context = {'indexes': indexes}
    return render(request, "gpw/index.html", context)


def download_index(request):

    url = 'https://www.bankier.pl/inwestowanie/profile/quote.html?symbol=MWIG40'
    page = get(url)
    bs = BeautifulSoup(page.content, 'html.parser')

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

        obj = Index.objects.filter(name=name_index).update(number=price_index)

        number += 1
        if number == 5:
            break

    context = {}
    return render(request, "gpw/download_index.html", context)
