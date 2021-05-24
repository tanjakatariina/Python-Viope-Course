# Luvun viimeinen tehtävä liittyy muistikirjan käsittelyyn. Tällä kertaa ohjelmaa muutetaan siten,
# että ohjelma lisää muistikirjamerkinnän perään päiväyksen ja kellonajan, josta käy ilmi milloin merkintä on
# tehty.Lisäksi laita viestin ja päiväyksen väliin eroitin ":::" (kolme kaksoispistettä).

# Päiväys saadaan esimerkiksi time-moduulista komennolla

# >>> import time
# >>> time.strftime("%X %x")
# '19:01:34 01/03/09'
# >>>

# joka palauttaa kellonajan ja päiväyksen merkkijonona. Kun tämä merkkijono liitetään viestiin,
# saadaan ohjelma toimimaan muodossa:

# (1) Lue muistikirjaa
# (2) Lisää merkintä
# (3) Tyhjennä muistikirja
# (4) Lopeta
#
# Mitä haluat tehdä?: 2
# Kirjoita uusi merkintä: -Soita Ekille
# (1) Lue muistikirjaa
# (2) Lisää merkintä
# (3) Tyhjennä muistikirja
# (4) Lopeta
#
# Mitä haluat tehdä?: 1
# -Soita Ekille:::19:06:39 01/03/09
#
# (1) Lue muistikirjaa
# (2) Lisää merkintä
# (3) Tyhjennä muistikirja
# (4) Lopeta
#
# Mitä haluat tehdä?: 4
# Lopetetaan.

import time

tiedoston_nimi = "muistio.txt"

try:
    tiedosto = open(tiedoston_nimi, "r")
    tiedosto.close()
except IOError:
    print("Oletusmuistioa ei löydy, luodaan tiedosto.")

while True:
    print("(1) Lue muistikirjaa\n(2) Lisää merkintä\n(3) Tyhjennä muistikirja\n(4) Lopeta\n")

    valinta = int(input("Mitä haluat tehdä?: "))

    if (valinta == 1):
        tiedosto = open(tiedoston_nimi, "r")
        sisalto = tiedosto.read()
        print(sisalto)
        tiedosto.close()
    elif (valinta == 2):
        tiedosto = open(tiedoston_nimi, "a")
        lisays = input("Kirjoita uusi merkintä: ")
        aika = time.strftime("%X %x")
        tiedosto.write(lisays + ":::" + aika)
        tiedosto.close()
    elif (valinta == 3):
        tiedosto = open(tiedoston_nimi, "w")
        print("Muistio tyhjennetty.")
        tiedosto.close()
    elif (valinta == 4):
        print("Lopetetaan.")
        break
    else:
        print("Tuntematon valinta")
