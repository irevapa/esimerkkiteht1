import random
oikea = random.randint(1, 10)
while True:
    arvaus = int(input("Arvaa luku 1-10: "))
    if arvaus < oikea:
        print("Liian pieni arvaus")
    elif arvaus > oikea:
        print("Liian suuri arvaus")
    else:
        print("Oikein! :)")
        break
