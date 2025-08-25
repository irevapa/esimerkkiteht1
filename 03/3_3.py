sukupuoli = (input("Syötä sukupuolesi: "))
hemoglobiini = int(input("Syötä hemoglobiinisi: "))

if sukupuoli == "nainen" :
    if hemoglobiini < 117 :
        print("alhainen")
    elif hemoglobiini > 175 :
        print("korkea")
    else: print("normaali")

if sukupuoli == "mies" :
    if hemoglobiini < 134 :
        print("alhainen")
    elif hemoglobiini > 195 :
        print("korkea")
    else: print("normaali")


