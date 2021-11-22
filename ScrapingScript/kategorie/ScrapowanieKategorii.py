import os
from requests import get
from bs4 import BeautifulSoup
from kategorie.Kategoria import Kategoria


def scrapuj_kategorie(lista_kategorii, url, id):

    backend_image ='https://cdn.pixabay.com/photo/2019/09/22/16/20/backend-4496461_1280.png'
    frontend_image = 'https://codecondo.com/wp-content/uploads/2017/08/Front-end-development-languages.jpg'
    it_image = 'https://www.soft-pc.pl/images/szkolenia.png'
    zdalne_image = 'https://www.alx.pl/media/kursy-zdalne-laptop.png'
    srednio_image = 'http://strefakarier.pl/wp-content/uploads/2019/02/kurs-komputerowy-czestochowa-400x200.jpg'
    black_friday_image = 'https://visionexpress.pl/promocje/wp-content/uploads/sites/3/2021/10/black_friday_960_504.jpg'

    # Pobranie strony
    strona = get(url)
    bs = BeautifulSoup(strona.content, 'html.parser')
    kategoria = bs.find('section', {"id": 'main'})
    nazwa = kategoria.find('h1', {"class": 'h1'}).get_text()
    zdjecie = ''

    if nazwa == 'Kursy BACK-END':
        zdjecie = backend_image
    elif nazwa == 'Kursy FRONT-END':
        zdjecie = frontend_image
    elif nazwa == 'Kursy IT':
        zdjecie = it_image
    elif nazwa == 'Kursy ZDALNE':
        zdjecie = zdalne_image
    elif nazwa == 'Kursy dla średnio zaawansowanych':
        zdjecie = srednio_image
    elif nazwa == 'Black Friday 2021':
        zdjecie = black_friday_image


    opis = kategoria.find('div', {"id": 'category-description'}).get_text()
    opis = opis.replace('\n', ' ')

    kursy = []
    modul_kursow = kategoria.find('div', {'class': 'products row'})
    wszystkie = modul_kursow.find_all('h3', {'class': 'h3 product-title'})

    for x in wszystkie:
        if x.get_text() == 'JS, React, Redux dla...':
            kursy.append('JS, React, Redux dla Programistów')
        elif x.get_text() == 'SCRUMstudy Scrum Developer...':
            kursy.append('SCRUMstudy Scrum Developer Certified (SDC™)')
        elif x.get_text() == 'Docker - Wstęp do...':
            kursy.append('Docker - Wstęp do Konteneryzacji')
        else:
            kursy.append(x.get_text())

    # Stworzenie nowego obiektu Kategoria i dodanie go do listy
    lista_kategorii.dodaj_kategorie(Kategoria(id, nazwa, opis, zdjecie, kursy))
