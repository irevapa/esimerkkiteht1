luvut = []
while True:
    syöte = input("Anna luku (tyhjä lopettaa): ")
    if syöte == "":
        break
    luvut.append(float(syöte))

luvut.sort(reverse=True)
print("Viisi suurinta lukua:")
for luku in luvut[:5]:
    print(luku)
