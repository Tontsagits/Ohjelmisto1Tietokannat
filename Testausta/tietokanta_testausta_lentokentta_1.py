# Tietokanta testausta - ihmiset - lisää random hakuja

# ladattavat kirjastot

import mysql.connector

# omat funktiot

def hae_lentokentta_icao_koodilla(icao):
    sql = f"SELECT name, municipality FROM airport WHERE ident = %s"
    # print(sql)
    kursori = db_lentopeli.cursor(dictionary=True)
    kursori.execute(sql, (icao,))
    return kursori.fetchone()

# main pääohjelma

db_lentopeli = mysql.connector.connect(
    host='localhost',
    port= 3306,
    database='flight_game',
    user='tontsah',
    password='tontsah1234',
    autocommit=True
)

koodi = input('Syötä lentokentän ICAO koodi: ')
lentokentta = hae_lentokentta_icao_koodilla(koodi)
if lentokentta is not None:
    print(f"{lentokentta['name']} on paikkakunnalla {lentokentta['municipality']}")
else:
    print('lentokenttää ei löytynyt')
