import csv
from requests import get
from bs4 import BeautifulSoup
from produkty.ScrapowanieProduktow import scrapujProdukt

class ListaProduktow:
    wszystkie_produkty = []
    naglowek = ['id', 'aktywny', 'nazwa', 'kategorie', 'cena', 'w sprzedazy', 'ilosc', 'dostepne_do_zamowienia', 'zdjecie', 'opis', 'stan', 'miasto', 'tryb', 'data', 'pakiet', 'platnosc', 'zalezny_od_stanu']

    def dodaj_produkt(self, produkt):
        self.wszystkie_produkty.append(produkt)

    def scrapuj_wszystkie_kursy(self, url):
        strona = get(url)
        bs = BeautifulSoup(strona.content, 'html.parser')

        paginacje = bs.find('nav', {'class': 'pagination'})
        paginacje = paginacje.find_all('a', {'rel': 'nofollow'})
        iterator = 1

        for x in paginacje:
            zmienna = get(x['href'])
            zmienna1 = BeautifulSoup(zmienna.content, 'html.parser')
            kursy = zmienna1.find_all('li', {'class': 'product_item col-xs-12 col-sm-6 col-md-6 col-lg-4'})
            for link in kursy:
                scrapujProdukt(self, link.find('a')['href'], iterator)
                iterator += 1

    def drukuj_produkty(self):
        for x in self.wszystkie_produkty:
            x.drukuj()

    def zaladuj_do_csv(self):
        with open('produkty.csv', 'w', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(self.naglowek)
            for x in self.wszystkie_produkty:
                writer.writerow(x.konwersja_na_liste())
