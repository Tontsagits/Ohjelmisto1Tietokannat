# Looppien testausta, For silmukka, Range funktio

for luku in range(3,31,3):
    print (luku)

for luku in range(6):
    print ("Moi!")


nimet = []
nimet = ["Matti", "Maija", "Molla", "Matias", "Joonas", "Turenki"]
nimet2 = ["Eppu", "Heppu", "Reppu", "Nekku", "Meininki", "Raja-arvo", "Askelvirhe", "Kaksoiskuljetus"]
print("Nimet")
print(nimet)
print("Nimet 2")
print(nimet2)
nimet.extend(nimet2)
print("Nimet extended")
print(nimet)
etunimi = input("Anna ensimmäinen nimi tai lopeta painamalla Enter: ")
while etunimi != "":
    nimet.append(etunimi)
    etunimi = input("Anna seuraava nimi tai lopeta painamalla Enter: ")

for nimi in nimet:
    print (f"Moi, {nimi}!")

for n in nimet:
    print (f"Moi, {n}!")

