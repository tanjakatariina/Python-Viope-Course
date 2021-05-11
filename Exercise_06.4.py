luku_1 = int(input("Anna luku: "))
luku_2 = int(input("Anna toinen luku: "))

if luku_1 % 2 == 0 and luku_2 % 2 == 0:
    print("Molemmat luvut ovat parillisia.")
elif luku_1 % 2 == 0 or luku_2 % 2 == 0:
    print("Toinen luku on parillinen.")
else:
    print("Molemmat luvut ovat parittomia.")
