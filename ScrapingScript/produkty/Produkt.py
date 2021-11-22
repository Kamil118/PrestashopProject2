class Produkt:
    def __init__(self, id, nazwa, zdjecie, stan, miasto, tryb, data, pakiet, platnosc,
                  cena, opis):
        self.id = id
        self.aktywny = 1
        self.w_sprzedazy = 0
        self.ilosc = 10000
        self.dostepne_do_zamowienia = 1
        self.nazwa = nazwa
        self.zdjecie = zdjecie
        self.stan = stan
        self.miasto = miasto
        self.tryb = tryb
        self.data = data
        self.pakiet = pakiet
        self.platnosc = platnosc
        self.cena = cena
        self.opis = opis
        self.kategorie = []
        self.zalezny_od_stanu = 0

    def kategorie_na_string(self):
        napis = ''
        for x in self.kategorie:
            napis += (x + '|')
        napis = napis[:-1]
        return napis

    def drukuj(self):
        print('Id: ',  self.id)
        print('Aktywny: ',  self.aktywny)
        print('W sprzedazy: ',  self.w_sprzedazy)
        print('Ilosc: ',  self.ilosc)
        print('Dostepne do zamowienia: ',  self.dostepne_do_zamowienia)
        print('Nazwa: ' + self.nazwa)
        print('Zdjecie: ' + self.zdjecie)
        print('Stan: ' + self.stan)
        print('Miasto: ' + self.miasto)
        print('Tryb: ' + self.tryb)
        print('Data: ' + self.data)
        print('Pakiet: ' + self.pakiet)
        print('Platnosc: ' + self.platnosc)
        print('Cena: ' + self.cena)
        print('Opis: ' + self.opis)
        print('Kategorie: ' + self.kategorie_na_string())
        print('Zalezny od stanu: ', self.zalezny_od_stanu)


   # ['id', 'aktywny', 'nazwa', 'kategorie', 'cena', 'w sprzedazy', 'ilosc', 'dostepne_do_zamowienia', 'zdjecie', 'opis',
   #  'stan', 'miasto', 'tryb', 'data', 'pakiet', 'platnosc']
    def konwersja_na_liste(self):
        lista = []
        lista.append(self.id)
        lista.append(self.aktywny)
        lista.append(self.nazwa)
        lista.append(self.kategorie_na_string())
        lista.append(self.cena)
        lista.append(self.w_sprzedazy)
        lista.append(self.ilosc)
        lista.append(self.dostepne_do_zamowienia)
        lista.append(self.zdjecie)
        lista.append(self.opis)
        lista.append(self.stan)
        lista.append(self.miasto)
        lista.append(self.tryb)
        lista.append(self.data)
        lista.append(self.pakiet)
        lista.append(self.platnosc)
        lista.append(self.zalezny_od_stanu)

        return lista
