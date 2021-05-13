tiedoston_nimi = str(input("Minkäniminen tiedosto luodaan?: "))
teksti = str(input("Mitä kirjoitetaan tiedostoon?: "))

try:
    tiedosto = open(tiedoston_nimi, "w")
    tiedosto.write(teksti)
    tiedosto.close()
    print("Luotiin tiedosto {0} ja siihen tallennettiin teksti: {1}".format(tiedoston_nimi, teksti))
except IOError:
    print("Error")
