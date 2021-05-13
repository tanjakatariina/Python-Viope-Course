# Kolmas tehtävä käyttää for-toistorakennetta. Tee ohjelma, joka pyytää käyttäjältä kierrosmäärän. Tämän jälkeen tee
# ohjelma, joka laskee kierroslukujen kertymän. Eli jos käyttäjä antaa syötteen 3, laskee ohjelma 0+1+2, jos 5
# niin 0+1+2+3+4. Lopuksi ohjelma tulostaa käyttäjälle lopputuloksen muodossa "Kertymäksi saatiin:" ja vastaus.

# Toimiessaan oikein ohjelma tulostaa seuraavaa:

# Kuinka monta kierrosta?: 3
# Kertymäksi saatiin: 3

# Tehtävässä kannattaa kokeilla kuinka kierrosluvun lisääminen muuttujaan toimii,
# eli vaikkapa tulos = tulos + kierrosluku.

kierrokset = int(input("Kuinka monta kierrosta?: "))

tulos = int(0)

for i in range(0, kierrokset):
    tulos += i

print("Kertymäksi saatiin: {0}".format(tulos))
