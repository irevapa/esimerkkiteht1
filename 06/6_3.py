def gallonatmuunnetaanlitroiksi(gallonat):
    return gallonat * 3.785

while True:
    gallonat = float(input("Anna gallonamäärä (negatiivinen lopettaa): "))
    if gallonat < 0:
        break
    print("Litroina:", gallonatmuunnetaanlitroiksi(gallonat))
