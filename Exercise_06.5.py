# Viimeinen tehtävä on jatkoa luvun 4. tehtävälle. Laajenna aiemmin aloittamaasi laskinta siten, että
# if-valintarakenteen avulla on mahdollista valita tehdäänkö luvuille yhteen- (valinta 1), vähennys- (valinta 2),
# kerto- (valinta 3) vai jakolasku (valinta 4).

# Lisäksi lisää ohjelman alkuun käyttäjälle ohje siitä, mitä eri valinnat tekevät, sekä ohjelmaan toiminto,
# millä ohjelma tulostaa "Valintaa ei tunnistettu", mikäli käyttäjä valitsee jotain muuta kuin valinnan väliltä 1-4.
# Tämä on helpointa toteuttaa else-osion avulla.

# Toimiessaan ohjelma toimii esimerkiksi seuraavalla tavalla:

# Anna ensimmäinen luku: 10
# Anna toinen luku: 40
# (1) +
# (2) -
# (3) *
# (4) /
# Tee valinta (1-4): 3
# Tulos on: 400

# Eli suorittaa halutun laskutoimituksen ja tulostaa vastauksen, tai mikäli valinta on virheellinen niin:

# Anna ensimmäinen luku: 101
# Anna toinen luku: 11
# (1) +
# (2) -
# (3) *
# (4) /
# Tee valinta (1-4): 100
# Valintaa ei tunnistettu.

luku_1 = int(input("Anna ensimmäinen luku: "))
luku_2 = int(input("Anna toinen luku: "))

print("""(1) +
(2) -
(3) *
(4) /""")

valinta = int(input("Tee valinta (1-4): "))

if valinta == 1:
    print("Tulos on:", luku_1 + luku_2)
elif valinta == 2:
    print("Tulos on:", luku_1 - luku_2)
elif valinta == 3:
    print("Tulos on:", luku_1 * luku_2)
elif valinta == 4:
    print("Tulos on:", luku_1 / luku_2)
else:
    print("Valintaa ei tunnistettu.")
