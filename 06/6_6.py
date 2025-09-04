import math

def yksikköhinta(halkaisija, hinta):
    sade_m = (halkaisija / 2) / 100  # muutetaan metreiksi :DD
    pinta_ala = math.pi * sade_m**2
    return hinta / pinta_ala

d1 = float(input("Anna 1. pizzan halkaisija (cm): "))
h1 = float(input("Anna 1. pizzan hinta (euroa): "))
d2 = float(input("Anna 2. pizzan halkaisija (cm): "))
h2 = float(input("Anna 2. pizzan hinta (euroa): "))

p1 = yksikköhinta(d1, h1)
p2 = yksikköhinta(d2, h2)

print(f"Pizza 1: {p1:.2f} €/m^2")
print(f"Pizza 2: {p2:.2f} €/m^2")

if p1 < p2:
    print("Pizza 1 antaa paremman vastineen rahallesi :).")
else:
    print("Pizza 2 antaa paremman vastineen rahallesi. :)")
