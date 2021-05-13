# Tässä tehtävässä kokeillaan merkkijonon leikkaamista. Määrittele muuttuja, joka sisältää merkkijonon
# "Hattukauppias". Tämän jälkeen ota siitä leikkaukset, joissa on A) neljä ensimmäistä kirjainta B) neljä viimeistä
# kirjainta ja C) merkkijono väärinpäin.

# Tulosta vastaus muodossa:

# Muuttujan 4 ensimmäistä kirjainta ovat Hatt
# Muuttujan 4 viimeistä kirjainta ovat pias
# Muuttujan teksti on väärinpäin saippuakuttaH

muuttuja = "Hattukauppias"

leikkaus_1 = muuttuja[:4]
leikkaus_2 = muuttuja[-4:]
leikkaus_3 = muuttuja[::-1]

print("Muuttujan 4 ensimmäistä kirjainta ovat", leikkaus_1)
print("Muuttujan 4 viimeistä kirjainta ovat", leikkaus_2)
print("Muuttujan teksti on väärinpäin", leikkaus_3)
