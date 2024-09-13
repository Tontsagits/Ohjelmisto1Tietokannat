# Ohjelmisto 1 - Moduuli 8 - Tehtävä 3 - Lentokenttien väliset etäisyydet


# ladattavat kirjastot

import mysql.connector
import geopy.distance

# omat funktiot

def laske_kenttien_etaisyys(tunnus1, tunnus2):
    kysely = f"SELECT ident, latitude_deg, longitude_deg FROM airport WHERE ident = %s;"
    # print(kysely)
    kursori = db_lentopeli.cursor()
    kursori.execute(kysely, (tunnus1,))
    tulos1 = kursori.fetchone()
    # print(tulos1)
    koordinaatti1 = tulos1[1], tulos1[2]
    # print(koordinaatti1)
    kursori.execute(kysely, (tunnus2,))
    tulos2 = kursori.fetchone()
    # print(tulos2)
    koordinaatti2 = tulos2[1], tulos2[2]
    # print(koordinaatti2)
    distance = geopy.distance.geodesic(koordinaatti1, koordinaatti2).kilometers
    if kursori.rowcount > 0 :
        # print(f"{tulos1[0]}, {tulos2[0]}, {distance}")
        return tulos1[0], tulos2[0], distance
    else:
        return None


# main pääohjelma

db_lentopeli = mysql.connector.connect(
    host='localhost',
    port= 3306,
    database='flight_game',
    user='tontsah',
    password='tontsah1234',
    autocommit=True
)

icaot1 = input('Syötä ensimmäisen lentokentän ICAO tunnus: ')
icaot2 = input('Syötä ensimmäisen lentokentän ICAO tunnus: ')
etaisyys = laske_kenttien_etaisyys(icaot1, icaot2)
if etaisyys is not None:
    print(f"Kenttien {etaisyys[0]} ja {etaisyys[1]} välinen etäisyys on {etaisyys[2]:.2f} km.")
else:
    print('Lentokenttiä ei löytynyt.')
