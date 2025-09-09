vuodenajat = ("kevät", "kesä", "syksy", "talvi")

kuukausi = int(input("Anna kuukauden numero (1-12): "))

if 3 <= kuukausi <= 5:
    vuodenaika = vuodenajat[0]
elif 6 <= kuukausi <= 8:
    vuodenaika = vuodenajat[1]
elif 9 <= kuukausi <= 11:
    vuodenaika = vuodenajat[2]
else:
    vuodenaika = vuodenajat[3]

print(f"Vuodenaika on {vuodenaika}.")
