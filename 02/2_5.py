# ohjelma, joka kysyy käyttäjältä massan keskiaikaisten mittojen mukaan leivisköinä, nauloina ja luoteina

leiviskä2 = float(input("syötä lieviskät: "))
naula2 = float(input("syötä naulat: "))
luoti2 = float(input("syötä luodit: "))

leiviskä = leiviskä2 * 20
naula = naula2 * 32 + leiviskä
luoti = luoti2 * 13.33 + naula

print("kokonaismassa on: ", luoti)

