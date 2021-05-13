# Tehtävä käsittelee tyyppimuunnoksia. Luodaan kaksi muuttujaa, joille annetaan arvoiksi 10.6411 ja "Merkkijono". Tee
# numeroarvon sisältävälle muuttujalle int()-tyyppimuunnos, ja kerro merkkijono kahdella.

# Tämän jälkeen laita ohjelmasi tulostamaan saamasi vastaukset muodossa:

# Kokonaislukumuunnos ei osaa pyöristää: 10
# Merkkijonon kertominen tuottaa toistoa: MerkkijonoMerkkijono

numero_muuttuja = 10.6411
merkkijono_muuttuja = "Merkkijono"

numero_muuttuja = int(numero_muuttuja)
merkkijono_muuttuja = merkkijono_muuttuja * 2

print("Kokonaislukumuunnos ei osaa pyöristää:", numero_muuttuja)
print("Merkkijonon kertominen tuottaa toistoa:", merkkijono_muuttuja)
