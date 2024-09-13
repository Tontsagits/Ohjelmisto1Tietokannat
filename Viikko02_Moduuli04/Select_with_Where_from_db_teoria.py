# Select from db - Ohjelmisto 1 Tietokannat - Teoria vko 2 moduuli 4
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
    database='ankkalinna',
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

# luotu ensin ankkalinna tietokanta

# Teoria

# select etunimi, sukunimi
# from ankkalinnalainen, lemmikki, omistaa
# where omistaa.ankkalinnalainen_id = ankkalinnalainen.id
# and omistaa.lemmikki_id = lemmikki.id
# and lemmikki.nimi = "Pulivari";
