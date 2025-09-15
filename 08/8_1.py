# task8_1.py
import mysql.connector

import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="pythonuser",
    password="MySecurePassword",
    database="lento"
)

cursor = conn.cursor()

icao = input("Anna ICAO-koodi: ").upper()
cursor.execute("SELECT name, municipality FROM airport WHERE ident = %s", (icao,))
result = cursor.fetchone()

if result:
    name, municipality = result
    print(f"Lentokenttä: {name}, Kunta: {municipality}")
else:
    print("Lentokenttää ei löytynyt.")

cursor.close()
conn.close()