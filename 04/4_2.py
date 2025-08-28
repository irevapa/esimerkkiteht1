while True:
    tuuma = float(input("Syötä tuumamäärä (negatiivinen lopettaa ohjelman): "))
    if tuuma < 0:
        break
    cm = tuuma * 2.54
    print(f"{tuuma} tuumaa = {cm} cm")
