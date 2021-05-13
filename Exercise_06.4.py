# Neljännessä tehtävässä harjoitellaan usean parametrin käyttämistä valintalauseessa. Tässä tehtävässä
# laajennetaan ensimmäistä tehtävää, ja otetaan mukaan toinen luku. Jos yksi käyttäjän syöttämistä luvuista on
# parillinen, tulostetaan "Toinen luku on parillinen", jos molemmat niin "Molemmat luvut on parillisia."
# Mikäli kumpikaan käyttäjän antama luku ei ole parillinen, tulostetaan "Molemmat luvut ovat parittomia."

# Ohjelma tulostaa toimiessaan seuraavanlaisia vastauksia:

# Anna luku: 10
# Anna toinen luku: 11
# Toinen luku on parillinen.

# tai vaihtoehtoisesti:

# Anna luku: 12
# Anna toinen luku: 20
# Molemmat luvut ovat parillisia.

# tai vaihtoehtoisesti:

# Anna luku: 13
# Anna toinen luku: 15
# Molemmat luvut ovat parittomia.

luku_1 = int(input("Anna luku: "))
luku_2 = int(input("Anna toinen luku: "))

if luku_1 % 2 == 0 and luku_2 % 2 == 0:
    print("Molemmat luvut ovat parillisia.")
elif luku_1 % 2 == 0 or luku_2 % 2 == 0:
    print("Toinen luku on parillinen.")
else:
    print("Molemmat luvut ovat parittomia.")
