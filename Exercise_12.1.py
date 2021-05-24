# Tämän luvun tehtävissä keskitytään Pythonin tehokkaimpaan sarjalliseen tietomuotoon, eli listaan. Ensimmäinen
# tehtävä onkin lyhyt perehdytys listan käyttämiseen. Muodosta lista, jossa on neljä alkioita, joilla on arvot
# "Sininen", "Punainen", "Keltainen" ja "Vihreä". Tämän jälkeen ota listasta leikkaus jossa on 1. alkio (paikalta 0),
# sekä tulosta listan kaikki alkiot for-lausetta apuna käyttäen.

# Toimiessaan ohjelma tulostaa seuraavaa:

# Listan ensimmäinen alkio on: Sininen
# Lista tulostettuna alkio kerrallaan:
# Sininen
# Punainen
# Keltainen
# Vihreä

lista = ["Sininen", "Punainen", "Keltainen", "Vihreä"]

print("Listan ensimmäinen alkio on: {}".format(lista[0]))

print("Lista tulostettuna alkio kerrallaan:")

for i in lista:
    print(i)
