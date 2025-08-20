# ohjelma, joka kysyy suorakulmion kannan ja korkeuden
kanta = float(input("Anna suorakulmion kanta: "))
korkeus = float(input("Anna suorakulmion korkeus: "))

# lasketaan pinta-ala
ala = kanta * korkeus

#tulostetaan vastaus
print(f"Pinta-ala on {ala:.2f}")