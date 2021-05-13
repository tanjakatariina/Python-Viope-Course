# Tässä tehtävässä kirjoitetaan tiedostoon. Tee ohjelma, joka ensin pyytää käyttäjältä tiedoston nimen, ja tämän
# jälkeen tekstin, jonka käyttäjä haluaa tiedostoon kirjoitettavan. Tämän jälkeen ohjelma tekee tiedoston,
# kirjoittaa tuloksen ja antaa ilmoituksen "Luotiin tiedosto [tiedostonnimi] ja siihen tallennettiin teksti: [sisältö]."

# Toimiessaan oikein ohjelma tulostaa vaikkapa seuraavan tekstin:

# Minkäniminen tiedosto luodaan?: loki.txt
# Mitä kirjoitetaan tiedostoon?: Attencion, attencion. 10, 10, 22, 33, Adios.
# Luotiin tiedosto loki.txt ja siihen tallennettiin teksti: Attencion, attencion. 10, 10, 22, 33, Adios.

tiedoston_nimi = str(input("Minkäniminen tiedosto luodaan?: "))
teksti = str(input("Mitä kirjoitetaan tiedostoon?: "))

try:
    tiedosto = open(tiedoston_nimi, "w")
    tiedosto.write(teksti)
    tiedosto.close()
    print("Luotiin tiedosto {0} ja siihen tallennettiin teksti: {1}".format(tiedoston_nimi, teksti))
except IOError:
    print("Error")
