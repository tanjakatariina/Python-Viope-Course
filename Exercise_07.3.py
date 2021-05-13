kierrokset = int(input("Kuinka monta kierrosta?: "))

tulos = int(0)

for i in range(0, kierrokset):
    tulos += i

print("Kertymäksi saatiin: {0}".format(tulos))
