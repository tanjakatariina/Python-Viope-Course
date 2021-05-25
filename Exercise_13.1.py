# Luvun 10 tehtävissä ei enää koodata varsinaisesti toiminnallisia ohjelmia, vaan kokeillaan erilaisten
# esimerkkikoodien avulla luokkamäärittelyn tekemistä ja olioiden perustoimintoja. Tämä sen vuoksi, että kurssi ei
# varsinaisesti keskity olio-ohjelmointiin, vaan pyrkii ainoastaan ohjaamaan siinä alkuun ja ymmärtämään miten se
# eroaa proseduraalisesta ohjelmoinnista.

# Ensimmäisessä oliotehtävässä luodaan määritellään luokkaa nimeltä Kilpailija, jolle annettaan kaksi jäsenmuuttujaa,
# pisteet ja vari. Tämän jälkeen luo luokasta olio "eka", jolle annetaan muuttujan vari arvoksi sininen ja pisteet
# arvoksi 10. Lopuksi laita ohjelmasi vielä tulostamaan olion tiedot muodossa "Kilpailijalla [väri] on [pisteet]
# pistettä!", eli näin:

# Kilpailijalla sininen on 10 pistettä!

class kilpailija:
    """Luokka määrittelee kilpailijan pisteet ja värin"""

    __pisteet = 0
    __vari = ""

    def lisaa_pisteet(self, lisays=1):
        self.__pisteet = + lisays

    def lisaa_vari(self, valinta):
        self.__vari = valinta

    def tulostus(self):
        print("Kilpailijalla {0} on {1} pistettä!".format(self.__vari, self.__pisteet))


def main():
    eka = kilpailija()
    eka.lisaa_vari("Sininen")
    eka.lisaa_pisteet(10)
    eka.tulostus()


if __name__ == "__main__":
    main()
