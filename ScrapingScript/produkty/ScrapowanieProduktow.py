import os
from requests import get
from bs4 import BeautifulSoup
from produkty.Produkt import Produkt


def scrapujProdukt(lista_produktow, url, id):

    # Pobranie strony

    strona = get(url)
    bs = BeautifulSoup(strona.content, 'html.parser')
    kurs = bs.find('section', {'id': 'main'})

    # NAZWA
    nazwa = kurs.find('h1', class_='h1 productpage_title')
    if nazwa:
        nazwa = nazwa.get_text()
    else:
        nazwa = ''

    # STAN
    stan = kurs.find('div', class_='product-condition')
    if stan:
        span = stan.find('span')
        if span:
            stan = span.get_text()
        else:
            stan = ''
    else:
        stan = ''

    if stan == 'Nowy Produkt':
        stan = 'new'
    else:
        stan = 'used'

    # ZDJECIE
    zdjecie = kurs.find('div', class_='product-cover')
    zdjecie = zdjecie.find('a')['href']

    # MIASTO
    miasto = kurs.find('select', {"id": 'group_5'})
    if miasto:
        miasto = miasto.find('option', {'selected': 'selected'}).get_text()
    else:
        miasto = ''

    # TRYB
    tryb = kurs.find('select', {"id": 'group_6'})
    if tryb:
        tryb = tryb.find('option', {'selected': 'selected'}).get_text()
    else:
        tryb = ''

    # DATA ROZPOCZĘCIA KURSU
    data = kurs.find('select', {"id": 'group_7'})
    if data:
        data = data.find('option', {'selected': 'selected'}).get_text()
    else:
        data = ''

    # Pakiet

    pakiet = kurs.find('select', {"id": 'group_8'})
    if pakiet:
        pakiet = pakiet.find('option', {'selected': 'selected'}).get_text()
    else:
        pakiet = ''

    # RODZAJ PLATNOSCI

    platnosc = kurs.find('select', {"id": 'group_9'})
    if platnosc:
        platnosc = platnosc.find('option', {'selected': 'selected'}).get_text()
    else:
        platnosc = ''

    # CENA
    cena = kurs.find('div', {'class': 'current-price'})
    cena = cena.find('span')
    if cena:
        cena = cena['content'] + ' zl'
    else:
        cena = '0 zl'

    # OPIS

    # opis = kurs.find('div', {'id': 'tab-content'})
    opis1 = kurs.find('div', {'class': 'product-description'})
    opis1 = opis1.get_text()

    opis2 = kurs.find('div', {'class': 'product-reference'})
    opis2 = opis2.get_text()

    opis = opis1 + '\n\n' + opis2
    opis = opis.replace('\n', '<br/>')
    # opis = "\"" + schowek + "\""

    # STWORZENIE NOWEGO OBIEKTU PRODUKT I DODANIE GO DO LISTY PRODUKTOW
    lista_produktow.dodaj_produkt(
        Produkt(id, nazwa, zdjecie, stan, miasto, tryb, data, pakiet, platnosc, cena, opis))
