luku = int(input("Syötä kokonaisluku: "))

if luku < 2:
    print("Ei alkuluku")
else:
    for i in range(2, int(luku**0.5) + 1):
        if luku % i == 0:
            print("Ei alkuluku :(")
            break
    else:
        print("Alkuluku :)")
