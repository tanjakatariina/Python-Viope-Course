# Kolmas esimerkki on ensimmäinen tehtävä, jossa luodaan käyttäjälle valikko. Käyttäjältä pyydetään luku
# väliltä 1-3, ja sen mukaan, mitä käyttäjä valitsee tulostetaan joko "Haukion kala Oy" valinnalla 1,
# "Metallipaja VasaraAika" valinnalla 2 tai "Balin palapelitehdas" valinnalla 3.

# Toimiessaan ohjelma tulostaa esimerkiksi seuraavaa:

# Valitse kohde (1-3): 1
# Haukion kala Oy

valinta_1 = "Haukion kala Oy"
valinta_2 = "Metallipaja VasaraAika"
valinta_3 = "Balin palapelitehdas"

kohde = int(input("Valitse kohde (1-3): "))

if 0 < kohde < 4:
    if kohde == 1:
        print(valinta_1)
    elif kohde == 2:
        print(valinta_2)
    else:
        print(valinta_3)
else:
    print("Epäkelvollinen syöte")
