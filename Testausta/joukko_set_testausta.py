# Joukko eli Set - testausta
# määrittelemätön joukko, ei voi viitata indeksillä
# vain uniikkeja arvoja, ei voi olla kahta samaa arvoa
# ei tarvitse olla samaa tyyppiä, voi olla eri tyyppisiä, numeroista, merkkejä, listoja, toisia tupleja
# tyhjä joukko luodaan funktiolla set()

print()

pelit = set()

pelit = {"Monopoli", "Shakki", "Cluedo"}
print(pelit)

pelit.add("Dominion")
print(pelit)

pelit.remove("Shakki")
print(pelit)

pelit.add("Cluedo")
print(pelit)

for p in pelit:
    print(p)

nimet = set()
nimet.add("Viivi")
print(nimet)
