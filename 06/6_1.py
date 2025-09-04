import random

def nopanheitto():
    return random.randint(1,6)

while True:
    silmäluku = nopanheitto()
    print("Heitto:", silmäluku)
    if silmäluku == 6 :
        break
