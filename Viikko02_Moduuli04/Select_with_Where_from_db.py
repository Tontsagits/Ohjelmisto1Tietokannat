# Select from db with Where

import mysql.connector

def tee_kysely(sql_lauseke):
    kysely = f"{sql_lauseke}"
    # kysely = f"SELECT ident, latitude_deg, longitude_deg FROM airport WHERE ident = %s;"
    print(kysely)
    kursori = db_lentopeli.cursor()
    kursori.execute(kysely)
    tulos = kursori.fetchall()
    # print(tulos)
    if kursori.rowcount > 0 :
        return tulos
    else:
        return None

db_lentopeli = mysql.connector.connect(
    host='localhost',
    port= 3306,
    database='flight_game',
    user='tontsah',
    password='tontsah1234',
    autocommit=True
)

kysely = input("Anna SQL kysely: ")
vastaus = tee_kysely(kysely)
if vastaus is not None:
    for rivi in vastaus:
        print(f'{rivi}')
else:
    print('Jotain meni pieleen.')
