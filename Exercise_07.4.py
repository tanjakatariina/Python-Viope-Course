luku_1 = int(input("Anna ensimmäinen luku: "))
luku_2 = int(input("Anna toinen luku: "))

while True:

    print("""(1) +
(2) -
(3) *
(4) /
(5) Vaihda luvut
(6) Lopeta""")

    print("Valitut luvut: {0} {1}".format(luku_1, luku_2))
    valinta = int(input("Tee valinta (1-6): "))

    if valinta == 1:
        print("Tulos on:", luku_1 + luku_2)
    elif valinta == 2:
        print("Tulos on:", luku_1 - luku_2)
    elif valinta == 3:
        print("Tulos on:", luku_1 * luku_2)
    elif valinta == 4:
        print("Tulos on:", luku_1 / luku_2)
    elif valinta == 5:
        luku_1 = int(input("Anna uusi ensimmäinen luku: "))
        luku_2 = int(input("Anna uusi toinen luku: "))
    elif valinta == 6:
        break
    else:
        print("Valintaa ei tunnistettu.")
