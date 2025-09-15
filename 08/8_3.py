import mysql.connector
from geopy.distance import geodesic

conn = mysql.connector.connect(
    host="localhost",
    user="pythonuser",        
    password="MySecurePassword",
    database="lento"
)

cursor = conn.cursor()

icao1 = input("Anna ensimmäinen ICAO-koodi: ").upper().strip()
icao2 = input("Anna toinen ICAO-koodi: ").upper().strip()

def get_coords(icao):
    cursor.execute(
        "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s",
        (icao,)
    )
    result = cursor.fetchone()
    if result:
        return result
    else:
        return None

coords1 = get_coords(icao1)
coords2 = get_coords(icao2)

if not coords1:
    print(f"Lentokenttää {icao1} ei löytynyt.")
elif not coords2:
    print(f"Lentokenttää {icao2} ei löytynyt.")
else:
    distance_km = geodesic(coords1, coords2).kilometers
    print(f"Etäisyys lentokenttien {icao1} ja {icao2} välillä: {distance_km:.2f} km")

cursor.close()
conn.close()
