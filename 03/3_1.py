kuha = float(input("Syötä kuhan pituus: "))
if kuha <37:
    kuha = 37 - kuha
    print(f"Kuha on {kuha} cm liian lyhyt.")

else: print("Kuha on hyvän pituinen!")