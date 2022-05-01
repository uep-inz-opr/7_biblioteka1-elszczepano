class Biblioteka:
    ksiazki = []
    egzemplarze = []

    def _get_ksiazka(self, tytul, autor):
        for ksiazka in self.ksiazki:
            if ksiazka.tytul == tytul and ksiazka.autor == autor:
                return ksiazka
        return False


    def dodaj_egzemplarz_ksiazki(self, tytul, autor, rok_wydania ):
        ksiazka = self._get_ksiazka(tytul, autor)

        if ksiazka == False:
            ksiazka = Ksiazka(tytul, autor)

            self.ksiazki.append(ksiazka)

        self.egzemplarze.append(Egzemplarz(ksiazka, rok_wydania))

class Ksiazka:
    def __init__(self, tytul, autor):
        self.tytul = tytul
        self.autor = autor

class Egzemplarz:
    def __init__(self, ksiazka_ref, rok_wydania):
        self.ksiazka_ref = ksiazka_ref
        self.rok_wydania = rok_wydania
        self.wypozyczony = False
    
books_count = int( input() )

biblioteka = Biblioteka()

for index in range(0, books_count):
    book = input().replace('(', '').replace(')', '').replace(' "', '').replace('"', '').split(",")

    biblioteka.dodaj_egzemplarz_ksiazki(book[0],book[1],book[2])

for ksiazka in biblioteka.ksiazki:
    counter = 0

    for egzemplarz in biblioteka.egzemplarze:
        if egzemplarz.ksiazka_ref is ksiazka:
            counter += 1

        print(f"('{ksiazka.tytul}', '{ksiazka.autor}', {str(counter)})")
