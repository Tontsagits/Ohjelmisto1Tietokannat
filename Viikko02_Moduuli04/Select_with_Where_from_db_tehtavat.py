# Select from db - Ohjelmisto 1 Tietokannat - Tehtävät vko 2 moduuli 4

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

# Tehtävät

# 1
# select country.name as 'country name', airport.name as 'airport name'
# from country, airport
# where country.iso_country = airport.iso_country
# and country.name = "Iceland";

# 2
# select airport.name as 'airport name'
# from country, airport
# where country.iso_country = airport.iso_country
# and country.name = "France"
# and airport.type = "large_airport";

# 3
# select country.name as 'country_name', airport.name as 'airport_name'
# from country, airport
# where country.iso_country = airport.iso_country
# and country.continent = "AN"
# order by country.name, airport.name;


# 4
# select airport.elevation_ft
# from airport, game
# where game.location = airport.ident
# and game.screen_name = "Heini";

# 5
# select airport.elevation_ft * 0.3048 as 'elevation_m'
# from airport, game
# where game.location = airport.ident
# and game.screen_name = "Heini";

# 6
# select airport.name as 'name'
# from airport, game
# where game.location = airport.ident
# and game.screen_name = "Ilkka";

# 7
# select country.name as 'name'
# from airport, game, country
# where game.location = airport.ident
# and airport.iso_country = country.iso_country
# and game.screen_name = "Ilkka";

# 8
# select goal.name as 'name'
# from game, goal_reached, goal
# where game.id = goal_reached.game_id
# and goal_reached.goal_id = goal.id
# and game.screen_name = "Heini";

# 9
# select *
# from game, goal_reached, goal
# where game.id = goal_reached.game_id
# and goal_reached.goal_id = goal.id
# and game.screen_name = "Ilkka";
#
# select * from goal;
#
# select game.screen_name
# from game, goal_reached, goal
# where goal.id = goal_reached.goal_id
# and goal_reached.game_id = game.id
# and goal.name = "CLOUDS";

# 10
#


