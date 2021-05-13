tiedosto = open("merkkijonoja.txt", "r")
sisalto = tiedosto.readlines()

for i in sisalto:
    i = i[:-1]
    if i.isalnum() == True:
        print("{0} kelpaa salasanaksi.".format(i))
    else:
        print("{0} sisältää virheellisiä merkkejä.".format(i))

tiedosto.close()
