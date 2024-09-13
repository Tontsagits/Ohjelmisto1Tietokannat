# Looppien testausta, While, For, mukana If ehtolause

# while kunnes ehto ei totta
kerrat = int(input("Montako kertaa tervehditään: "))
tehdyt = 0
while tehdyt<kerrat:
    print("Hyvää huomenta")
    tehdyt = tehdyt + 1

# while, käyttäjä lopettaa
komento = input ("Anna komento ('lopeta' lopettaa): ")
while komento!="lopeta":
    print ("Suoritan toiminnon: " + komento)
    komento = input("Anna komento: ")
print ("Toiminnot lopetettu.")


# while else
komento = input ("Anna komento: ")
while komento!="lopeta":
    if komento=="MAYDAY":
        break
    print ("Suoritan toiminnon: " + komento)
    komento = input("Anna komento: ")
else:
    print ("Näkemiin.")
print ("Toiminnot lopetettu.")



# while kunnes ehto1 tai ehto2 ei totta
from random import randint
noppa1 = noppa2 = heitot = 0
while (noppa1!=6 or noppa2!=6):
    noppa1 = randint(1,6)
    noppa2 = randint(1,6)
    heitot = heitot + 1
print(f"Tarvittiin {heitot:d} heittoa.")


# sisäiset while loopit
eka = 1
while eka <= 5:
    toka = 1
    while toka <= 5:
        print(f"{eka} kertaa {toka} on {eka*toka:d}")
        toka = toka + 1
    eka = eka + 1

# if elif else
ikä = int(input("Anna ikäsi: "))
if ikä>=65:
    print("Olet eläkeiässä.")
elif ikä>=18:
    print("Olet työiässä.")
elif ikä>=7:
    print("Olet koululainen.")
else:
    print("Olet pikkulapsi.")



