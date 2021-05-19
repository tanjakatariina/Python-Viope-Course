# Neljäs tehtävä lisää ohjelmaan paluuarvon. Tee ohjelma, jossa on pääfunktio main ja alifunktio pituusmitta.
# pituusmitta saa syötteenä parametrin ja mittaa tämän parametrin pituuden, palauttaen sen integer-arvona pääohjelmalle.

# Pääohjelma pyytää käyttäjältä syötettä "Anna syote (Lopeta lopettaa): " ja lähettää syötteen mitattavaksi.
# Jos tulos on 0, ohjelma vastaa "Et antanut syötettä", muuten "Antamasi syöte oli [pituus] merkkiä pitkä.".
# Jos käyttäjä antaa arvon Lopeta, ohjelma sammuu.

# Ohjelma tulostaa seuraavaa:

# Anna syöte (Lopeta lopettaa): sihijuomaa
# Antamasi syöte oli 10 merkkiä pitkä.
# Anna syöte (Lopeta lopettaa): nahkasaapasharja
# Antamasi syöte oli 16 merkkiä pitkä.
# Anna syöte (Lopeta lopettaa):
# Et antanut syötettä
# Anna syöte (Lopeta lopettaa): Lopeta

def main():
    while True:
        syote = input("Anna syöte (Lopeta lopettaa): ")
        syote_pituus = pituusmitta(syote)
        if syote == "Lopeta":
            break
        elif syote_pituus == 0:
            print("Et antanut syötettä")
        else:
            print("antamasi syöte oli {0} merkkiä pitkä".format(syote_pituus))


def pituusmitta(pituus):
    pituus = len(pituus)
    return int(pituus)


if __name__ == "__main__":
    main()
