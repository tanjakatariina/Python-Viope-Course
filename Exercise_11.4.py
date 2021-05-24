# Tässä tehtävässä jatketaan laskin tehtävää. Tehtävässä lisätään laskimeen kaksi uutta tehtävää, sin ja cos.
# Nämä funktiot löytyvät math-moduulin sisältä, vastaavilla funktionimillä sin() ja cos(), joille molemmille
# voidaan antaa syötteeksi (luku_1 / luku_2). Toteuta käskyt vaihtoehdoiksi 5 ja 6, samalla siirtäen "vaihda luvut" ja
# "Lopeta" kohdiksi 7 ja 8.

# Ohjelma toimii seuraavalla tavalla:

# Anna ensimmäinen luku: 1
# Anna toinen luku: 2
# (1) +
# (2) -
# (3) *
# (4) /
# (5)sin(luku1/luku2)
# (6)cos(luku1/luku2)
# (7)Vaihda luvut
# (8)Lopeta
# Valitut luvut: 1 2
# Tee valinta (1-8): 5
# Tulos on: 0.479425538604
# (1) +
# (2) -
# (3) *
# (4) /
# (5)sin(luku1/luku2)
# (6)cos(luku1/luku2)
# (7)Vaihda luvut
# (8)Lopeta
# Valitut luvut: 1 2
# Tee valinta (1-8): 6
# Tulos on: 0.87758256189
# (1) +
# (2) -
# (3) *
# (4) /
# (5)sin(luku1/luku2)
# (6)cos(luku1/luku2)
# (7)Vaihda luvut
# (8)Lopeta
# Valitut luvut: 1 2
# Tee valinta (1-8): 8

import math

luku_1 = int(input("Anna ensimmäinen luku: "))
luku_2 = int(input("Anna toinen luku: "))

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
        luku_1 = int(input("Anna uusi ensimmäinen luku: "))
        luku_2 = int(input("Anna uusi toinen luku: "))
    elif valinta == 8:
        break
    else:
        print("Valintaa ei tunnistettu.")
