# Tässä tehtävässä jatketaan edellistä tehtävää. Muuta ohjelmaasi siten, että luokalla Kilpailija on kaksi
# jäsenfunktiota, tilanne ja maali. Kutsuttaessa funktiota tilanne olio tulostaa "Olen [vari] ja minulla on [pisteet]
# pistettä!". Kutsuttaessa funktiota maali olio lisää itselleen yhden pisteen.

# Pääohjelma luo luokasta olion nimeltä "eka" ja antaa sille muuttujan eka.vari arvoksi "sininen". Lopuksi ohjelma
# kutsuu ensin jäsenfunktiota eka.maali() ja lopuksi funktiota eka.tilanne().

# Ohjelma tulostaa siis seuraavaa:

# Olen sininen ja minulla on 1 pistettä!

class kilpailija:
    """Luokka määrittelee kilpailijan pisteet ja värin"""

    __pisteet = 0
    __vari = ""

    def lisaa_pisteet(self, lisays=1):
        self.__pisteet = + lisays

    def lisaa_vari(self, valinta):
        self.__vari = valinta

    def tilanne(self):
        print("Olen {0} ja minulla on {1} pistettä!".format(self.__vari, self.__pisteet))

    def maali(self):
        self.__pisteet = + 1


def main():
    eka = kilpailija()
    eka.lisaa_vari("sininen")
    eka.maali()
    eka.tilanne()


if __name__ == "__main__":
    main()
