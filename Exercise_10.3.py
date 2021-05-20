# Luvun kolmas tehtävä jatkaa edellisessäkin luvussa työstettyä nelilaskinta. Tähän asti ohjelma on ollut sen varassa,
# että käyttäjä antaa aina laskimelle oikeita lukuarvoja, mutta virheenkäsittelyn avulla tämäkin ongelma voidaan
# poistaa.

# Tee siis ohjelmakoodiin muutokset, joilla käyttäjän antamat syötteet tarkastetaan ennen kuin ne hyväksytään laskimeen
# numeroiksi. Helpointa tämä on tehdä luomalla erillinen alifunktio, joka pyytää käyttäjältä niin kauan uutta lukua
# kunnes tyyppimuunnos kokonaisluvuksi onnistuu. Tämän jälkeen alifunktio palauttaa lukuarvon laskimelle. Jos käyttäjän
# syöttämä luku on virheellinen, tulostetaan "Virheellinen syöte!" ja lukua pyydetään uudestaan.

# Toimiessaan oikein ohjelma tulostaa vaikkapa seuraavaa:

# Anna luku: fge
# Virheellinen syöte!
# Anna luku: 10
# Anna luku: 15
# (1) +
# (2) -
# (3) *
# (4) /
# (5)sin(luku1/luku2)
# (6)cos(luku1/luku2)
# (7)Vaihda luvut
# (8)Lopeta
# Valitut luvut: 10 15
# Tee valinta (1-8): 7
# Anna luku: apina
# Virheellinen syöte!
# Anna luku: 20
# Anna luku: 9
# (1) +
# (2) -
# (3) *
# (4) /
# (5)sin(luku1/luku2)
# (6)cos(luku1/luku2)
# (7)Vaihda luvut
# (8)Lopeta
# Valitut luvut: 20 9
# Tee valinta (1-8): 8

import math


def syote():
    while True:
        try:
            luku = int(input("Anna luku: "))
            break
        except ValueError:
            print("Virheellinen syöte!")
            continue

    return luku


luku_1 = syote()
luku_2 = syote()

while True:
    print("(1) +\n(2) -\n(3) *\n(4) /\n(5) sin(luku1/luku2)\n(6) cos(luku1/luku2)\n(7) Vaihda luvut\n(8) Lopeta")

    print("Valitut luvut: {0} {1}".format(luku_1, luku_2))
    valinta = int(input("Tee valinta (1-8): "))

    if valinta == 1:
        print("Tulos on:", luku_1 + luku_2)
    elif valinta == 2:
        print("Tulos on:", luku_1 - luku_2)
    elif valinta == 3:
        print("Tulos on:", luku_1 * luku_2)
    elif valinta == 4:
        print("Tulos on:", luku_1 / luku_2)
    elif valinta == 5:
        print("Tulos on:", math.sin(luku_1 / luku_2))
    elif valinta == 6:
        print("Tulos on:", math.cos(luku_1 / luku_2))
    elif valinta == 7:
        luku_1 = syote()
        luku_2 = syote()
    elif valinta == 8:
        break
    else:
        print("Valintaa ei tunnistettu.")
