# Kurssin viimeinen proseduraaliseen ohjelmointiin liittyvä tehtävä on eräänlainen päättötyö, joka kokoaa kaikki
# kurssilla käsitellyt asiat yhteen kokonaisuuteen. Tässä tehtävässä muokataan muistikirja-harjoitustehtävää
# viimeisen kerran. Koska ohjelman rakenne muuttuu melko paljon, myös "puhtaalta pöydältä" aloittaminen on
# ihan järkevä vaihtoehto.

# Työssä rakennetaan muistikirja, joka käyttää merkintöjen hallintaan Pythonin lista-tietorakennetta sekä tallentaa
# muistikirjan bittimuotoisena tietokoneen levylle. Ohjelmassa on seuraavat ominaisuudet:
# A) Ohjelmaan voidaan lisätä merkintöjä, joissa on samanlainen aikaleima kuin aiemmin.
# B)Ohjelmassa voi valita merkinnän listalta, ja korvata sen uudella.
# C)Ohjelmalla voi poistaa yksittäisen merkinnän listalta, sekä
# D)Ohjelma lataa aiemmin luodun listan ohjelman käynnistyessä mikäli sellainen on olemassa.

# Ohjelma käyttää tietokantanaan tiedostoa nimeltä "muistio.dat". Käynnistyessään ohjelma koittaa ladata aiemmin luodun
# listan ko. tiedostosta, tai mikäli tällaista ei ole olemassa tai sen lataaminen tuottaa virheen, luo uuden ilmoittaen
# "Virhe tiedostossa, luodaan uusi muistio.dat.". Tämän jälkeen käyttäjä voi lisätä merkintljä listalle kuten aiemmin:

# Virhe tiedostossa, luodaan uusi muistio.dat.
# (1) Lue muistikirjaa
# (2) Lisää merkintä
# (3) Muokkaa merkintää
# (4) Poista merkintä
# (5) Tallenna ja lopeta
#
# Mitä haluat tehdä?: 2
# Kirjoita uusi merkintä: -Osta kananmunia
# (1) Lue muistikirjaa
# (2) Lisää merkintä
# (3) Muokkaa merkintää
# (4) Poista merkintä
# (5) Tallenna ja lopeta
#
# Mitä haluat tehdä?: 2
# Kirjoita uusi merkintä: -Osta perunoita

# Käyttäjä voi myös halutessaan muuttaa yksittäistä merkintää valinnalla 3. Tämän jälkeen ohjelma ilmoittaa listalla
# olevien merkintöjen määrän "Listalla on [määrä] merkintää." Pyytää käyttäjältä muutettavan merkinnän numeron
# "Mitä niistä muutetaan?:". Käyttäjä ilmoittaa haluamansa luvun ja voi tämän jälkeen vaihtaa tekstin ja saa uuden
# aikamerkinnän. Huomaa, että pyydettäessä numeroa ohjelma ymmärtää luvun 1 tarkoittavan ensimmäistä merkintää
# eli listan alkiota [0].

# (1) Lue muistikirjaa
# (2) Lisää merkintä
# (3) Muokkaa merkintää
# (4) Poista merkintä
# (5) Tallenna ja lopeta
#
# Mitä haluat tehdä?: 3
# Listalla on 2 merkintää.
# Mitä niistä muutetaan?: 1
# -Osta kananmunia:::14:52:54 01/04/09
# Anna uusi teksti: -Osta tärpättiä

# Tietueen poisto listalta toimii samalla tavalla kuin muokkaus. Ainoa ero on siinä, että ohjelma tulostaa käyttäjälle
# tiedon siitä, mikä merkintä listalta poistettiin tulosteella "Poistettiin merkintä [merkintä]".

# (1) Lue muistikirjaa
# (2) Lisää merkintä
# (3) Muokkaa merkintää
# (4) Poista merkintä
# (5) Tallenna ja lopeta
#
# Mitä haluat tehdä?: 4
# Listalla on 2 merkintää.
# Mitä niistä poistetaan?: 2
# Poistettiin merkintä -Osta perunoita:::14:53:00 01/04/09

# Lopuksi käyttäjän lopettaessa listalla olevat merkinnät tallennetaan pickle-moduulia apunakäyttäen tiedostoon
# "muistio.dat" ja tulostaa "Lopetetaan.".

# (1) Lue muistikirjaa
# (2) Lisää merkintä
# (3) Muokkaa merkintää
# (4) Poista merkintä
# (5) Tallenna ja lopeta
#
# Mitä haluat tehdä?: 5
# Lopetetaan.

# Jos ohjelma käynnistetään uudelleen, ladataan aiemmalla käyttökerralla luodut merkinnät tiedostosta "muistio.dat",
# jolloinka niitä voidaan käyttää myös toisella käyttökerralla. Lisäksi, jos käyttäjä haluaa lukea muistikirjaa,
# tulostaa ohjelma listan alkiot allekkain:

# (1) Lue muistikirjaa
# (2) Lisää merkintä
# (3) Muokkaa merkintää
# (4) Poista merkintä
# (5) Tallenna ja lopeta
#
# Mitä haluat tehdä?: 1
# -Osta tärpättiä:::14:53:16 01/04/09
# (1) Lue muistikirjaa
# (2) Lisää merkintä
# (3) Muokkaa merkintää
# (4) Poista merkintä
# (5) Tallenna ja lopeta
#
# Mitä haluat tehdä?: 5
# Lopetetaan.

import time
import pickle

tiedoston_nimi = "muistio.dat"
lista = []

try:
    tiedosto = open(tiedoston_nimi, "rb")
    lista = pickle.load(tiedosto)
    tiedosto.close()
except IOError:
    print("Virhe tiedostossa, luodaan uusi muistio.dat.")
    tiedosto = open(tiedoston_nimi, "wb")

while True:
    print("(1) Lue muistikirjaa\n(2) Lisää merkintä\n(3) Muokkaa merkintää\n(4) Poista merkintä\n(5) Tallenna ja "
          "lopeta\n")

    valinta = int(input("Mitä haluat tehdä?: "))

    if (valinta == 1):
        for i in lista:
            print(i)
    elif (valinta == 2):
        lisays = input("Kirjoita uusi merkintä: ")
        aika = time.strftime("%X %x")
        kokonaisuus = lisays + ":::" + aika
        lista.append(kokonaisuus)
        pickle.dump(lista, tiedosto)
    elif (valinta == 3):
        try:
            pituus = len(lista)
            print("Listalla on {0} merkintää.".format(pituus))
            muutos_valinta = int(input("Mitä niistä muutetaan?: "))
            muutos_valinta = muutos_valinta - 1
            print(lista[muutos_valinta])
        except IndexError:
            print("Virheellinen valinta.")
        else:
            uusi_teksti = input("Anna uusi teksti: ")
            aika = time.strftime("%X %x")
            kokonaisuus = uusi_teksti + ":::" + aika
            lista.pop(muutos_valinta)
            lista.insert(muutos_valinta, kokonaisuus)
            tiedosto = open(tiedoston_nimi, "wb")
            pickle.dump(lista, tiedosto)
            tiedosto.close()
    elif (valinta == 4):
        pituus = len(lista)
        print("Listalla on {0} merkintää.".format(pituus))
        poisto_valinta = int(input("Mitä niistä poistetaan?: "))
        try:
            poisto_valinta = poisto_valinta - 1
            print("Poistettiin merkintä {0}".format(lista[poisto_valinta]))
            lista.pop(poisto_valinta)
            tiedosto = open(tiedoston_nimi, "wb")
            pickle.dump(lista, tiedosto)
            tiedosto.close()
        except IndexError:
            print("Virheellinen valinta.")
    elif (valinta == 5):
        tiedosto = open(tiedoston_nimi, "wb")
        pickle.dump(lista, tiedosto)
        print("Lopetetaan.")
        tiedosto.close()
        break
    else:
        print("Tuntematon valinta")
