import csv
from requests import get
from bs4 import BeautifulSoup
from kategorie.ScrapowanieKategorii import scrapuj_kategorie
from kategorie import Kategoria

class ListaKategorii:

    wszystkie_kategorie = []
    naglowek = ['id', 'aktywny', 'nazwa', 'opis', 'zdjecie']

    def dodaj_kategorie(self, kategoria):
        self.wszystkie_kategorie.append(kategoria)

    def scrapuj_wszystkie_kategorie(self, url):
        strona = get(url)
        bs = BeautifulSoup(strona.content, 'html.parser')
        kategorie = bs.find('div', {"id": 'block_categories_toggle'})
        linki = kategorie.find('ul', {"class": 'category-sub-menu'})
        iterator = 1

        for link in linki.find_all('a'):
            scrapuj_kategorie(self, link['href'], iterator)
            iterator += 1

    def dodaj_kategorie_do_produktow(self, lista_produktow):
        for x in self.wszystkie_kategorie:
            for y in x.kursy:
                for z in lista_produktow:
                    if y == z.nazwa:
                        z.kategorie.append(x.nazwa)


    def drukuj_kategorie(self):
        for x in self.wszystkie_kategorie:
            x.drukuj()

    def zaladuj_do_csv(self):
        with open('kategorie.csv', 'w', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(self.naglowek)
            for x in self.wszystkie_kategorie:
                writer.writerow(x.konwersja_na_liste())
