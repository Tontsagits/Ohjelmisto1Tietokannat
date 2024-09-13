# Monikko eli Tuple - testausta
# muuttumaton eli ei mutatoituva, ei voi lisätä eikä poistaa alkioita luonnin jälkeen
# luenteeltaan siis staattinen

# esimerkki
print()

viikonpaivat = ("maanantai", "tiistai", "keskiviikko", "torstai", "perjantai", "lauantai", "sunnuntai")
jarjestysnumero = int(input("Anna viikonpäivän järjestysnumero (1-7): "))
viikonpaiva = viikonpaivat[jarjestysnumero-1]
print (f"{jarjestysnumero}. viikonpäivä on {viikonpaiva}.")

# ei tarvita sulkuja
hedelmät = "Appelsiini", "Banaani", "Omena"
print(hedelmät)

# esim. arvojen purkaminen monikon sisältä ulos
hedelmät = ("Appelsiini", "Banaani", "Omena")
(eka, toka, kolmas) = hedelmät
print (f"Hedelmiä ovat {eka}, {toka} ja {kolmas}.")

# monikko funktion paluuarvona
import random
def heitä():
    eka, toka = random.randint(1,6), random.randint(1,6)
    return eka, toka
noppa1, noppa2 = heitä()
print(f"Nopista tuli {noppa1} ja {noppa2}.")

