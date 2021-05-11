luku_1 = int(input("Anna ensimmäinen luku: "))
luku_2 = int(input("Anna toinen luku: "))

print("""(1) +
(2) -
(3) *
(4) /""")

valinta = int(input("Tee valinta (1-4): "))

if valinta == 1:
    print("Tulos on:", luku_1 + luku_2)
elif valinta == 2:
    print("Tulos on:", luku_1 - luku_2)
elif valinta == 3:
    print("Tulos on:", luku_1 * luku_2)
elif valinta == 4:
    print("Tulos on:", luku_1 / luku_2)
else:
    print("Valintaa ei tunnistettu.")
