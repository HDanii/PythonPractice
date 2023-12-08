import random
lottoGomb = []
kihuzottSzamok = []
tipp = []
#szam = 0
szamlalo = 0

for i in range(1, 5):
    szam = int(input("Adj meg egy számot 1 és 90 között: "))
    tipp.append(szam)   

for i in range(1, 91):
    lottoGomb.append(i)




random.shuffle(lottoGomb)


for i in range(0, 5):
    kihuzottSzamok.append(lottoGomb[i])


kihuzottSzamok.sort()
tipp.sort()

print(f"Az ön tippje: {tipp}")
print(f"A kihúzott számok: {kihuzottSzamok}")
