# Sanakirja Dictionary - testausta
# avain-arvo pareja
# arvo voi olla muu tietorakenne kuten vaikka toinen sanakirja tai lista tai tuple, tms.

# luodaan sanakirja
numerot = {"Viivi":"050-1234567",
           "Ahmed":"040-1112223",
           "Pekka":"050-7654321"}

# lisätään vielä lisää avain-arvo pareja
numerot["Olga"] = "050-1011012"
numerot["Mary"] = "0401-2132139"
numerot["Sofia"] = "044-3332211"

print()
print (numerot)

nimi = input("Anna nimi: ")
if nimi in numerot:
    print (f"Henkilön {nimi} puhelinnumero on {numerot[nimi]}.")

for avain in numerot:
    print(avain)

for avain, arvo in numerot.items():
    print(f"avain: {avain} arvo: {arvo}")
