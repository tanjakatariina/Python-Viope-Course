# Luvun viimeisessä tehtävässä jatkamme eteenpäin aiemmin tekemäämme laskinta. Tällä kertaa ohjelmaan tehdään seuraavat
# lisätoiminnot: (A) laskin ei sammu heti laskutoimituksen jälkeen, vaan käyttäjä voi valita useamman laskutehtävän
# ja ohjelma sammuu vasta kun käyttäjä valitsee 6, sekä (B) Käyttäjä voi valinnalla 5 vaihtaa käyttämänsä luvut.

# Toimiessaan ohjlma toimii esimerkiksi seuraavalla tavalla:

# Anna ensimmäinen luku: 10
# Anna toinen luku: 15
# (1) +
# (2) -
# (3) *
# (4) /
# (5)Vaihda luvut
# (6)Lopeta
# Valitut luvut: 10 15
# Tee valinta (1-6): 2
# Tulos on: -5
# (1) +
# (2) -
# (3) *
# (4) /
# (5)Vaihda luvut
# (6)Lopeta
# Valitut luvut: 10 15
# Tee valinta (1-6): 5
# Anna uusi ensimmäinen luku: 20
# Anna uusi toinen luku: 10
# (1) +
# (2) -
# (3) *
# (4) /
# (5)Vaihda luvut
# (6)Lopeta
# Valitut luvut: 20 10
# Tee valinta (1-6): 6

# Jälleen kerran koko varsinainen ohjelma kannattaa sijoittaa toistorakenteen sisään, jolloin katkaisu on helppo
# toteuttaa break-käskyllä.

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
