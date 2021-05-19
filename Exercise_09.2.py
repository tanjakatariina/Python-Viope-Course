# Toinen tehtävä liittyy alifunktion parametrien välitykseen. Tee tehtävä, jossa on pääfunktio main ja alifunktio
# "toinenpotenssi". Alifunktio ottaa vastaan yhden parametrin, laskee sille toisen potenssin ja tulostaa vastauksen
# muodossa "Toinen potenssi on [vastaus]". Pääohjelma vastaavasti pyytää käyttäjältä lukua "Anna lukuarvo: "
# ja lähettää sen eteenpäin alifunktiolle.

# Toimiessaan oikein ohjelma toimii seuraavalla tavalla:

# Anna lukuarvo: 10
# Toinen potenssi on 100

# Tai vaikkapa

# Anna lukuarvo: 123123
# Toinen potenssi on 15159273129

def main():
    lukuarvo = int(input("Anna lukuarvo: "))
    toinenpotenssi(lukuarvo)


def toinenpotenssi(luku):
    luku = luku ** 2
    print("Toinen potenssi on {0}".format(luku))


if __name__ == "__main__":
    main()
