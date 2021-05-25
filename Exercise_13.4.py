# Luvun ja samalla kurssin viimeisessä tehtävässä kokeillaan luokkien perimistä.

# Määrittele kaksi luokkaa nimeltä Emo ja Lapsi. Anna Emo-luokalle kaksi jäsenmuuttujaa, arvo ja tila, sekä
# jäsenfunktio nimi, jolla olio tulostaisi "Minä olen emoluokka". Anna muuttujalle arvo arvoksi 0, ja muuttujalle
# tila arvo "Toiminnassa".

# Vastaavasti Lapsi-luokka peritään Emo-luokasta. määrittele lapsiluokalle ylikirjoittava funktio nimi,
# jolla olio tulostaa "Minä olen lapsiluokka."

# Laita pääohjelma tekemään molemmista luokista oliot, joka jälkeen yritä tulostaa molempien olioiden
# tila-jäsenmuuttuja, sekä kutsu kummankin olion jäsenfunktiota nimi.

# Jos luokat on tehty oikein, tulostaa ohjelma näin:

# Toiminnassa
# Minä olen emoluokka.
# Toiminnassa
# Minä olen lapsiluokka.

class Emo:
    """Emoluokka"""
    arvo = 0
    tila = "Toiminnassa"

    def nimi(self):
        print("Minä olen emoluokka.")


class Lapsi(Emo):
    """Lapsiluokka"""

    def nimi(self):
        print("Minä olen lapsiluokka.")


def main():
    emo = Emo()
    lapsi = Lapsi()
    print(emo.tila)
    emo.nimi()
    print(lapsi.tila)
    lapsi.nimi()


if __name__ == "__main__":
    main()
