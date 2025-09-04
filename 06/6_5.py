def parilliset(lista):
    uusilista = []
    for luku in lista:
        if luku % 2 == 0:
            uusilista.append(luku)
    return uusilista

luvut = [1, 2, 3, 4, 5, 6]
print("Alkuperäinen:", luvut)
print("Parilliset:", parilliset(luvut))
