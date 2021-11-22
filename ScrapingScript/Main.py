from kategorie.ListaKategorii import ListaKategorii
from produkty.ListaProduktow import ListaProduktow
import csv
URL = 'https://sklep.coderslab.pl/index.php?id_category=10&controller=category'

lista_produktow = ListaProduktow()
lista_produktow.scrapuj_wszystkie_kursy(URL)

lista_kategorii = ListaKategorii()
lista_kategorii.scrapuj_wszystkie_kategorie(URL)

lista_kategorii.dodaj_kategorie_do_produktow(lista_produktow.wszystkie_produkty)
lista_kategorii.drukuj_kategorie()
lista_produktow.drukuj_produkty()

lista_kategorii.zaladuj_do_csv()
lista_produktow.zaladuj_do_csv()


