import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="pythonuser",
    password="MySecurePassword",
    database="lento"
)

cursor = conn.cursor()


country_code = input("Anna maakoodi: ").upper().strip()

query = """
SELECT type, COUNT(*) 
FROM airport
WHERE iso_country = %s
GROUP BY type;
"""

cursor.execute(query, (country_code,))

results = cursor.fetchall()

if results:
    print(f"Lentokentät maassa {country_code}:")
    for airport_type, count in results:
        print(f"{airport_type}: {count} kpl")
else:
    print(f"Maasta {country_code} ei löytynyt lentokenttiä.")

cursor.close()
conn.close()
