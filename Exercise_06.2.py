#  Tehtävässä luodaan kaksi if-else-rakennetta, joista toinen sijoitetaan ensimmäisen sisään. Ohjelmassa käyttäjältä
#  pyydetään nimi ja salasana. Jos nimi on väärin, tulostaa ohjelma "Nimi oli väärin.". Jos nimi on oikein, pyydetään
#  salasanaa. Jos salasana on oikein, tulostetaan "Salasana ja nimi oli oikein!", muussa tapauksessa
#  "Salasana oli väärin.". Toteuta oikeaksi nimi-salasana-pariksi Erkki ja Esimerkki.

#  Ohjelma tulostaa toimiessaan seuraavanlaisia vastauksia:

# Anna nimi: Petteri
# Nimi oli väärin.

# tai vaihtoehtoisesti:

# Anna nimi: Erkki
# Anna salasana: Kanada
# Salasana oli väärin.

# tai vaihtoehtoisesti:

# Anna nimi: Erkki
# Anna salasana: Esimerkki
# Salasana ja nimi oli oikein!

nimi = str(input("Anna nimi: "))

if nimi == "Erkki":
    salasana = input("Anna salasana: ")
    if salasana == "Esimerkki":
        print("Salasana ja nimi oli oikein!")
    else:
        print("Salasana oli väärin.")
else:
    print("Nimi oli väärin.")
