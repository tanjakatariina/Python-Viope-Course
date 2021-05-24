# Luvun ensimmäinen tehtävä perustuu random-moduulikirjaston toimintaan. Tee ohjelma, joka arpoo viisi kertaa joko
# luvun 0 tai 1 käyttäen random.randint-kirjastofunktiota. Mikäli ohjelma arpoo luvun 0, tulostetaan "Klaava!",
# mikäli 1 niin "Kruuna!". Ohjelma alkaa tulosteella "Heitetään kolikkoa viidesti:" ja

# toimii seuraavalla tavalla:

# Heitetään kolikkoa viidesti:
# Klaava!
# Kruuna!
# Kruuna!
# Kruuna!
# Kruuna!

from random import randint

print("Heitetään kolikkoa viidesti:")

i = 0

while i < 5:
    i += 1
    kolikko = randint(0, 1)
    if kolikko == 0:
        print("Klaava!")
    else:
        print("Kruuna!")
