# Kolmannessa tehtävässä Kilpailija-luokkaa muokataan kahdella tavalla. Ensinnäkin, kirjoita luokalle seliterivi
# "Kilpailija: sisältää pisteet ja värin". Toisekseen, lisää luokkaan alustusfunktio __init__, jossa uusi olio
# pyytää itselleen värin käyttäjän syötteenä "Anna minulle väri: ".
#
#
# Pääohjelmassa tulee luoda kaksi oliota ja antaa näille alustuksessa värit "sininen" ja "punainen", tämän jälkeen
# kutsuen molempien tilanne-jäsenfunktiota. Lopuksi ohjelma vielä tulostaa ensimmäisen olion selostetekstin komennolla
# print([nimi].__doc__).
#
# Ohjelma tulostaa siis seuraavaa:

# Anna minulle väri: sininen
# Anna minulle väri: punainen
# Olen sininen ja minulla on 0 pistettä!
# Olen punainen ja minulla on 0 pistettä!
# Kilpailija: sisältää pisteet ja värin

class kilpailija:
    """Kilpailija: sisältää pisteet ja värin"""

    __pisteet = 0
    __vari = ""

    def __init__(self):
        self.__vari = input("Anna minulle väri: ")

    def tilanne(self):
        print("Olen {0} ja minulla on {1} pistettä!".format(self.__vari, self.__pisteet))


def main():
    eka = kilpailija()
    toka = kilpailija()
    eka.tilanne()
    toka.tilanne()
    print(eka.__doc__)


if __name__ == "__main__":
    main()
