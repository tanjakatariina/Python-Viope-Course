# Lähdekooditiedoston kanssa samaan hakemistoon on tallennettuna tiedosto "merkkijonoja.txt". Tämä tiedosto sisältää
# satunnaisesti luotuja merkkijonoja, joissa esiintyy kahdenlaisia merkkijonoja: sellaisia, joissa on kirjaimia ja
# mahdollisesti numeroita, sekä sellaisia, joissa on kirjaimia, numeroita ja erikoismerkkejä (€,#,{, §, jne).
# Tehtävänäsi on tehdä ohjelma, joka lukee tiedostosta rivin, testaa onko merkkijono sellainen, joka sisältää vain
# kirjaimia ja numeroita, ja sen mukaan tulostaa joko "[merkkijono] kelpaa salasanaksi" jos on, tai "[merkkijono]
# sisältää virheellisiä merkkejä." mikäli siinä on ei-alfanumeerisia merkkejä.

# Toimiessaan ohjelma tulostaa seuraavaa:

# 5345m345ö34l kelpaa salasanaksi.
# no2no123non4 kelpaa salasanaksi.
# noq234n5ioqw#% sisältää virheellisiä merkkejä.
# %#""SGMSGSER sisältää virheellisiä merkkejä.
# doghdp5234 kelpaa salasanaksi.
# sg,dermoepm sisältää virheellisiä merkkejä.
# 43453-frgsd sisältää virheellisiä merkkejä.
# hsth())) sisältää virheellisiä merkkejä.
# bmepm35wae kelpaa salasanaksi.
# vmopaem2234+0+ sisältää virheellisiä merkkejä.
# gsdm12313 kelpaa salasanaksi.

# Tehtävässä kannattaa rivit lukea yksi kerrallaan ja testata .isalnum()-merkkijonometodilla. Lisäksi muista poistaa
# lopussa oleva rivinvaihtomerkki, se ei ole kirjain eikä numero!

tiedosto = open("merkkijonoja.txt", "r")
sisalto = tiedosto.readlines()

for i in sisalto:
    i = i[:-1]
    if i.isalnum() == True:
        print("{0} kelpaa salasanaksi.".format(i))
    else:
        print("{0} sisältää virheellisiä merkkejä.".format(i))

tiedosto.close()
