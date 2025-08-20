nimi = input("anna nimesi: ")

print("Moi, " + nimi)

# ohjelma, joka kysyy suorakaiteen
# kannan ja korkeuden, ja laskee
# niiden perusteella pinta-alan

# luetaan syötteet ja talletetaan arvot muuttujiin
kanta = float(input("Anna suorakaiteen kanta: "))
korkeus = float(input("Anna suorakaiteen korkeus: "))

# lasketaan pinta-ala
ala = kanta * korkeus

#tulostetaan vastaus
print(f"Pinta-ala on {ala:.2f}")
