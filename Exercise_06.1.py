# Tämän luvun tehtävät aloitetaan yksinkertaisen if-rakenteen luomisella. Ohjelma pyytää käyttäjältä luvun ja
# tallentaa sen muuttujaan. Mikäli luku on parillinen, ohjelma tulostaa vastauksen "Antamasi luku oli parillinen".
# If-rakenteen ehtolauseeseen tarvittavat parametrit löydät luvun taulukosta, ja helpoin tapa toteuttaa ohjelma
# onkin käyttää jakojäännös-operaattoria, testaten onko jakojäännös 0. Ohjelman ei tarvitse myöskään reagoida
# virheellisiin syötteisiin eikä desimaalilukuihin.

# Ohjelma tulostaa seuraavan vastauksen:

# Anna luku: 24
# Antamasi luku oli parillinen.

# tai vaihtoehtoisesti:

# Anna luku: 11

# Eli ei mitään, mikäli luku ei ole parillinen.

syote = int(input("Anna luku: "))

if (syote % 2) == 0:
    print("Antamasi luku oli parillinen.")
