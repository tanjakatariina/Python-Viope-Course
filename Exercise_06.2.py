nimi = str(input("Anna nimi: "))

if nimi == "Erkki":
    salasana = input("Anna salasana: ")
    if salasana == "Esimerkki":
        print("Salasana ja nimi oli oikein!")
    else:
        print("Salasana oli väärin.")
else:
    print("Nimi oli väärin.")
