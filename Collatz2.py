hatarertek = int(input("Kérem a határértéket: "))
lepesek = 0
leghosszabbSzekvencia = -1
leghosszabbSzekvSzam = -1
vizsgaltSzam = 0
legmagasabbSzam = 0
maximumVizsgaltSzam = 0


for szamlalo in range(2, hatarertek):
    szam = szamlalo
    vizsgaltSzam = szam
    while szam > 1:  
        if szam % 2 == 0:
            szam = int(szam/2)
            lepesek += 1
        else:
            szam = int((szam*3) + 1)
            lepesek += 1

        if leghosszabbSzekvencia < lepesek:
            leghosszabbSzekvencia = lepesek
            leghosszabbSzekvSzam = vizsgaltSzam
            print(f'Új leghosszab szekvenciát találtam: {leghosszabbSzekvencia} a viszgált szám: {leghosszabbSzekvSzam}')

        if legmagasabbSzam < szam:
            legmagasabbSzam = szam
            maximumVizsgaltSzam = vizsgaltSzam
            print(f'Új legmagasabb számot találtam: {legmagasabbSzam}, a vizsgált szám: {maximumVizsgaltSzam}')

    lepesek = 0
print(f'A leghosszabb sorozat: {leghosszabbSzekvencia}, a hozzá tartozó szám: {leghosszabbSzekvSzam}')
print(f'A legmagasabb szám: {legmagasabbSzam}, a hozzátartozó kiinduló érték: {maximumVizsgaltSzam}')

