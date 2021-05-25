# Luvun kolmannessa tehtävässä puhutaan listasta ja tiedostojen käsittelystä. Meillä on olemassa tiedosto "sanoja.txt",
# joka sisältää joukon erilaisia sanoja. Tehtävänäsi on lukea sanat muistiin, laittaa ne aakkosjärjestykseen ja tulostaa
# ruudulle allekkain selitteen "Sanat laitettuna aakkosjärjestykseen:" alle.

# Toimiessaan oikein ohjelma tulostaa vaikkapa seuraavaa:

# Sanat laitettuna aakkosjärjestykseen:
# aavikkorotta
# autokauppias
# hattuteline
# huono
# kaljakori
# kivitalo
# kumipallo
# lapio
# puuveistos
# rautanaula
# saunatonttu
# tuuli

# Kaikki sanat alkavat pienellä kirjaimella ja niiden jälkeen on rivinvaihto. Tehtävää varten kannattaa erityisesti
# tutustua listan metodiin .sort, sekä muistaa rivinvaihtojen poistaminen luetuista sanoista.

tiedosto = open("sanoja.txt", "r")
sisalto = tiedosto.readlines()

sisalto = [sana.strip() for sana in sisalto]
sisalto.sort()

print("Sanat laitettuna aakkosjärjestykseen:")

for i in sisalto:
    print(i)