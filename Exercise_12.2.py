# Toisessa tehtävässä luodaan ostoslista käyttäen Pythonin lista-tietomuotoa. Tee ohjelma, jossa käyttäjä voi (1)
# lisätä tuotteita listaan, (2) poistaa tuotteita listalta tai (3) lopettaa.

# Mikäli käyttäjä lisää tuotteen listaan, pyytää ohjelma syötteen "Mitä lisätään?: ") ja laittaa sen listan viimeiseksi
# alkioksi. Jos käyttäjä haluaa poistaa tuotteen, kertoo ohjelma "Listalla on [määrä] alkiota", ja käyttäjä antaa
# syötteen "Monesko niistä poistetaan?", jonka jälkeen ohjelma poistaa numeronmukaisen alkion (0 on siis 1. alkio).

# Jos käyttäjä lopettaa, tulostaa ohjelma "Listalla oli tuotteet:" ja listan sisällön kokonaisuudessaan allekkain.
# Virheelliseen valintaan reagoidaan tulostamalla rivi "Virheellinen valinta". Tämä koskee myös sitä jos käyttäjä
# valitsee poistettavan alkion listan ulkopuolelta.

# Toimiessaan ohjelma tulostaa seuraavaa:

# Haluatko
# (1)Lisätä listaan
# (2)Poistaa listalta vai
# (3)Lopettaa?: 1
# Mitä lisätään?: Omenoita
# Haluatko
# (1)Lisätä listaan
# (2)Poistaa listalta vai
# (3)Lopettaa?: 1
# Mitä lisätään?: Olutta
# Haluatko
# (1)Lisätä listaan
# (2)Poistaa listalta vai
# (3)Lopettaa?: 2
# Listalla on 2 alkiota.
# Monesko niistä poistetaan?: 0
# Haluatko
# (1)Lisätä listaan
# (2)Poistaa listalta vai
# (3)Lopettaa?: 3
# Listalla oli tuotteet:
# Olutta

lista = []

while True:
    valinta = int(input("Haluatko\n(1)Lisätä listaan\n(2)Poistaa listalta vai\n(3)Lopettaa?: "))
    if valinta == 1:
        lisays = input("Mitä lisätään?: ")
        lista.append(lisays)
    elif valinta == 2:
        try:
            pituus = len(lista)
            print("Listalla on {0} alkiota.".format(pituus))
            poisto = int(input("Monesko niistä poistetaan?: "))
            lista.pop(poisto)
        except IndexError:
            print("Virheellinen valinta.")
    elif valinta == 3:
        print("Listalla oli tuotteet: ")
        for i in lista:
            print(i)
        break
    else:
        print("Virheellinen valinta.")
