#  Funktioiden testausta

# funktion parametrit
def tervehdi(kerrat):
    for i in range(kerrat):
        print ("Hyvää päivää " + str(i+1) + ". kerran")
    return

print("Päivä alkaa tervehdyksillä.")
print("Tervehditään viisi kertaa")
tervehdi(5)
print ("Tervehditään vielä 2 kertaa lisää.")
tervehdi(2)
kaikki_kerrat = int(input("Montako kertaa tervehditään? "))
tervehdi(kaikki_kerrat)


# funktion sisäiset, paikalliset muuttujat ja globaalit muuttujat
def vaihda():
    kaupunki = "Vantaa"
    print("Funktiossa lopuksi: " + kaupunki)
    return

kaupunki = "Helsinki"
print("Pääohjelmassa aluksi: " + kaupunki)
vaihda()
print("Pääohjelmassa lopuksi: " + kaupunki)


# useita parametrejä
def tervehdi(tervehdys, kerrat):
    for i in range(kerrat):
        print (tervehdys + " " + str(i+1) + ". kerran")
    return
tervehdi("Moi", 3)
tervehdi("Hyvää päivää", 2)


# funktio paluuarvot
def neliösumma(eka, toka):
    ns = eka**2 + toka**2
    return ns

luku1 = float(input("Anna ensimmäinen luku: "))
luku2 = float(input("Anna toinen luku: "))
tulos = neliösumma(luku1, luku2)
print(f"Lukujen {luku1:.3f} ja {luku2:.3f} neliösumma on {tulos:.3f}.")

# lista funktion parametrina

def inventaario(tavarat):
    print("Sinulla on seuraavat tavarat:")
    for t in tavarat:
        print ("- " + t)
    return

reppu = ["Vesipullo", "Kartta", "Kompassi", "Puukko", "Taskulamppu", "Eväsrasia", "Viltti", "Makuupussi", "Pehmolelu"]
inventaario(reppu)
reppu.append("Linkkuveitsi")
inventaario(reppu)

