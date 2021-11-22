class Kategoria:

    def __init__(self, id, nazwa, opis, zdjecie, kursy):
        self.id = id
        self.aktywny = 1
        self.nazwa = nazwa
        self.opis = opis
        self.zdjecie = zdjecie
        self.kursy = kursy


    def kursy_na_string(self):
        napis = ''
        for x in self.kursy:
            napis += (x + ' |')
        napis = napis[:-2]
        return napis

    def drukuj(self):
        print('Id: ',  self.id)
        print('Aktywny: ',  self.aktywny)
        print('Nazwa: ' + self.nazwa)
        print('Opis: ' + self.opis)
        print('Zdjecie: ' + self.zdjecie)
        print('Kursy wchodzące w skład kategorii: ' + self.kursy_na_string())

    def zwroc_kursy(self):
        return self.kursy

    def konwersja_na_liste(self):
        lista = []
        lista.append(self.id)
        lista.append(self.aktywny)
        lista.append(self.nazwa)
        lista.append(self.opis)
        lista.append(self.zdjecie)
        return lista
