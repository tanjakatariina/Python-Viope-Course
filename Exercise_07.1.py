# Tämän luvun ensimmäinen tehtävä on yksinkertaisen while-rakenteen toteuttaminen. Tehtävänä onkin luoda ohjelma,
# joka tulostaa joka kierroksella kierrosluvun, millä tällä hetkellä ollan. Ohjelma aloittaa kierroksesta 0, ja
# jatkaa tästä eteenpäin 4 kierrosta.

# Toimiessaan ohjelma tulostaa seuraavan tekstin:

# Olemme kierroksella 0
# Olemme kierroksella 1
# Olemme kierroksella 2
# Olemme kierroksella 3
# Olemme kierroksella 4

# Toistorakenteen ehto kannattaa suunnitella kahta muuttujaa käyttäen, joista toinen määrää ylärajan ja toiseen
# lasketaan aina käynnissä oleva kierros.

ylaraja = 5
kierros = 0

while kierros < ylaraja:
    print("Olemme kierroksella {0}".format(kierros))
    kierros += 1
