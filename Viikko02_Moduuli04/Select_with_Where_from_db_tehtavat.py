# Select from db - Ohjelmisto 1 Tietokannat - Tehtävät vko 3 moduuli 4

import mysql.connector

def tee_kysely(sql_lauseke):
    sql_kysely = f"{sql_lauseke}"
    # kysely = f"SELECT ident, latitude_deg, longitude_deg FROM airport WHERE ident = %s;"
    print(sql_kysely)
    kursori = db_lentopeli.cursor()
    kursori.execute(sql_kysely)
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

# ajettu ensin lp.sql jolla luotiin flight_game tietokanta tietoineen

# 1 select * from goal;
# 2 select name, type from airport where iso_country = "FI";
# 3 select name, type from airport where iso_country = "FI" order by name asc;
# 4 select name, type from airport where iso_country = "FI" order by type asc, name asc;
# 5 select name from country where name like "F%";
# 6 select name from country where name like "%f%";
# 7 select ident as location from airport where ident = "EGCC";
# 8 select co2_consumed from game where screen_name = "Ilkka";
# 9 select co2_budget from game limit 1;
