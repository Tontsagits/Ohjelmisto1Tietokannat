# Lista olion testausta, listan elementit eli alkiot


print()

nimet = ["Viivi", "Ahmed", "Pekka", "Olga", "Mary", "Olavi", "Kermit", "Helmi", "Reipas"]

print(nimet[3])
print(nimet[1])
print(nimet[-2])
print(nimet[1:3])
print(nimet[2:])
print(nimet)
print()

nimet2 = ["Makke", "Jokke", "Unto", "Mertsi", "Kaaleppi", "Viktoria", "Anselmi", "Mei", "Lin"]
print(nimet2)
print()

nimet.append("Kuu-Ukko")
print(nimet)
print()

nimet.sort()
print(nimet)
print()

nimet.sort(reverse=True)
print(nimet)
print()

nimet.extend(nimet2)
print(nimet)
print()

for nimi in nimet:
    print(nimi)
print()
