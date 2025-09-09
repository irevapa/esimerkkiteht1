lentoasemat = {}

toiminto = input("Valitse toiminto (uusi, haku, lopeta): ")
while toiminto != "lopeta":
    if toiminto == "uusi":
        icao = input("Anna ICAO-koodi: ")
        nimi = input("Anna lentoaseman nimi: ")
        lentoasemat[icao] = nimi
    elif toiminto == "haku":
        icao = input("Anna ICAO-koodi: ")
        if icao in lentoasemat:
            print(lentoasemat[icao])
        else:
            print("Tuntematon ICAO-koodi")
    toiminto = input("Valitse toiminto (uusi, haku, lopeta): ")
