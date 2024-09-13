# Select from db - Ohjelmisto 1 Tietokannat - Teoria vko 2 moduuli 3
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

# luodaan ankkalinna tietokanta
# create database ankkalinna;
# use ankkalinna;
# create table ankkalinnalainen ( ID int not null auto_increment, etunimi varchar(40), sukunimi varchar(40), primary key (id) );
# create table lemmikki ( ID int not null auto_increment, nimi varchar(40), primary key (id) );
# create table omistaa ( lemmikki_ID int, ankkalinnalainen_ID int, primary key (lemmikki_ID,ankkalinnalainen_ID), foreign key (lemmikki_ID) references lemmikki(ID), foreign key (ankkalinnalainen_ID) references ankkalinnalainen(ID) );
# insert into ankkalinnalainen (etunimi, sukunimi) values ("Aku", "Ankka"), ("Roope", "Ankka"), ("Tupu", "Ankka"), ("Milla", "Magia"), ("Mikki", "Hiiri");
# insert into lemmikki (nimi) values ("Pulivari"), ("Pluto"), ("Korri");
# insert into omistaa (lemmikki_ID, ankkalinnalainen_ID) values(1,1),(1,3),(2,5),(3,4);

# insert into ankkalinnalainen (etunimi, sukunimi) values ("Hessu", "Hopo"), ("Polle", "Koninkaulus");
# select * from ankkalinnalainen;
# select * from ankkalinnalainen where sukunimi = "Ankka";
# select sukunimi from ankkalinnalainen where sukunimi like "%i%";
# select * from ankkalinnalainen order by sukunimi desc, etunimi desc;
# select * from ankkalinnalainen order by sukunimi asc, etunimi asc;
# select id as tunnistenumero, etunimi, sukunimi from ankkalinnalainen;
