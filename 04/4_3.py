luvut = []
while True:
    syöte = input("Anna luku (tyhjä lopettaa): ")
    if syöte == "":
        break
    luvut.append(float(syöte))

if luvut:
    print("Pienin:", min(luvut))
    print("Suurin:", max(luvut))
