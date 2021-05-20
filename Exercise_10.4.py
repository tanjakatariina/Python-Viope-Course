# Myös muistikirja on tähän asti toiminut sen varassa, että käyttäjä ei yritä lukea muistiota ennen kuin tiedostoon
# on kirjoitettu jotain. Tällä kertaa muistikirja-ohjelmaan lisätäänkin kaksi uutta toimintoa; ensinnäkin ohjelman
# tulee tarkastaa käynnistyessään onko tiedosto "muistio.txt" olemassa, ja tarvittaessa luoda tämänniminen tiedosto.
# Mikäli näin tehdään ilmoittaa ohjelma "Oletusmuistiota ei löydy, luodaan tiedosto".

# Toisekseen, lisää ohjelmaan mahdollisuus vaihtaa muistiotiedostoa kesken ohjelman suorituksen lisäämällä ohjelmaan
# valinta "(4) Vaihda muistiota", jonka jälkeen ohjelma pyytää uutta muistiotiedostoa "Anna tiedoston nimi: " ja
# tarvittaessa luo tämännimisen tiedoston jälleen antaen ilmoituksen "Tiedostoa ei löydy, luodaan tiedosto.".
# Lisäksi ohjelma kertoo päävalikossa mitä tiedostoa tällähetkellä käytetään; "Käytetään muistiota: [tiedostonnimi]".

# Toimiessaan oikein ohjelma tulostaa vaikkapa seuraavaa:

# Oletusmuistioa ei löydy, luodaan tiedosto.
# Käytetään muistiota:  muistio.txt
# (1) Lue muistikirjaa
# (2) Lisää merkintä
# (3) Tyhjennä muistikirja
# (4) Vaihda muistiota
# (5) Lopeta

# Mitä haluat tehdä?: 2
# Kirjoita uusi merkintä: -Osta maitoa
# Käytetään muistiota:  muistio.txt
# (1) Lue muistikirjaa
# (2) Lisää merkintä
# (3) Tyhjennä muistikirja
# (4) Vaihda muistiota
# (5) Lopeta

# Mitä haluat tehdä?: 4
# Anna tiedoston nimi: uusimuistio.txt
# Tiedostoa ei löydy, luodaan tiedosto.
# Käytetään muistiota:  uusimuistio.txt
# (1) Lue muistikirjaa
# (2) Lisää merkintä
# (3) Tyhjennä muistikirja
# (4) Vaihda muistiota
# (5) Lopeta

# Mitä haluat tehdä?: 2
# Kirjoita uusi merkintä: -Osta ananas
# Käytetään muistiota:  uusimuistio.txt
# (1) Lue muistikirjaa
# (2) Lisää merkintä
# (3) Tyhjennä muistikirja
# (4) Vaihda muistiota
# (5) Lopeta

# Mitä haluat tehdä?: 1
# -Osta ananas:::13:53:00 01/04/09

# Käytetään muistiota:  uusimuistio.txt
# (1) Lue muistikirjaa
# (2) Lisää merkintä
# (3) Tyhjennä muistikirja
# (4) Vaihda muistiota
# (5) Lopeta

# Mitä haluat tehdä?: 5
# Lopetetaan.

# Ohjelman toteuttamisessa kannattaa lähestyä ongelmaa siten, että käytettävän tiedoston nimi on tallennettuna
# muuttujaan, jonka arvoa muutetaan jos tiedostoa vaihdetaan. Lisäksi tiedoston olemassaolon tarkastun on helpointa
# toteuttaa yrittämällä avata tiedosto ja sulkemalla se samantien; jos ohjelma palauttaa IOErrorin voidaan samanniminen
# tiedosto luoda kirjoitustilalla.

import time

tiedoston_nimi = "muistio.txt"

try:
    tiedosto = open(tiedoston_nimi, "r")
    tiedosto.close()
except IOError:
    print("Oletusmuistioa ei löydy, luodaan tiedosto.")

while True:
    print("käytetään muistiota: {0}".format(tiedoston_nimi))
    print("(1) Lue muistikirjaa\n(2) Lisää merkintä\n(3) Tyhjennä muistikirja\n(4) Vaihda muistiota\n(5) Lopeta\n")

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
        tiedoston_nimi = input("Anna tiedoston nimi: ")
        try:
            tiedosto = open(tiedoston_nimi, "r")
            tiedosto.close()
        except IOError:
            print("Tiedostoa ei löydy, luodaan tiedosto.")
    elif (valinta == 5):
        print("Lopetetaan.")
        break
    else:
        print("Tuntematon valinta")
