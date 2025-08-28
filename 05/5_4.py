kaupungit = []
for _ in range(5):
    nimi = input("Syötä kaupunki: ")
    kaupungit.append(nimi)

print("Kaupungit syöttämässäsi järjestyksessä:")
for kaupunki in kaupungit:
    print(kaupunki)
