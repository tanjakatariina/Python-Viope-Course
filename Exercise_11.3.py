# Luvun neljäs tehtävä jatkaa oman moduulin tekemistä. Tässä tehtävässä luomme ohjelman, joka testaa käyttäjän
# syöttämiä merkkijonoja sen mukaan, kuinka ne soveltuisivat salasanoiksi. Myös tässä tehtävässä on tarkoitus
# ainoastaan toteuttaa moduuli olemassaolevalle ohjelmalle.

# Meillä on valmiina ohjelman pääfunktion sisältävä moduuli, jonka sisältö näyttää tältä:

# import tarkastaja
# while True:
#     testattava = input("Anna testattava sana: ")
#     tulos = tarkastaja.testaa(testattava)
#     if tulos == True:
#         print("Antamasi sana kelpaa salasanaksi!")
#         break
#     else:
#         print("Sana ei kelpaa.")

# Tehtäväsi onkin luoda tähän päämoduuliin sopiva tarkastaja-moduuli. Tee moduuli, jossa on testaa-niminen funktio,
# joka vastaanottaa syötteen. Jos syöte on alle 5 merkkiä pitkä, sisältää pelkästään kirjaimia tai pelkästään numeroita,
# palauttaa ohjelma False. Muussa tapauksessa ohjelma palauttaa arvon True. Ohjelma lopetetaan kun käyttäjä antaa
# ensimmäisen sopivan syötteen.
#
# Toimiessaan ohjelma tulostaa seuraavaa:

# Anna testattava sana: Testi
# Sana ei kelpaa.
# Anna testattava sana: 234234
# Sana ei kelpaa.
# Anna testattava sana: Testisana11234
# Antamasi sana kelpaa salasanaksi!

# Ohjelman ei tarvitse huomioida erikoismerkkien tilannetta, vaan ainoastaan tarkastaa, että merkkijono on 5 merkkiä
# tai enemmän, sekä sisältää numeroita ja kirjaimia. Merkkijonotestit .isalpha ja .isdigit ovat tässä
# tapauksessa hyödyllisiä apuvälineitä.

def testaa(syote):
    if len(syote) < 5 or syote.isalpha() or syote.isdigit():
        return False
    else:
        return True
