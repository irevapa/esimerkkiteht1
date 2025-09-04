import random

def nopanheitto(tahkoja):
        return random.randint(1, tahkoja)

tahkoja = int(input("Anna nopan tahkojen määrä:"))

while True:
        silmäluku = nopanheitto(tahkoja)
        print("Heitto:",silmäluku)
        if silmäluku == tahkoja :
            break