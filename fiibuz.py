
#for i in range(1, 100):
felsoHatar = int(input("Meddig nézzem a számokat? "))
i= 1
fiz = []
buz = []
fizbuz = []
fizbuzSzamokOszzege = 0
buzSzamokOszzege = 0
fizSzamokOszzege = 0

while i != felsoHatar:
    if i % 3 == 0 and i % 5 == 0:
        #print(f"Fizbuz ({i})")
        fizbuz.append(i)
    elif i % 3 == 0:
        #print(f"Fiz ({i})")
        fiz.append(i)
    elif i % 5 == 0:
        #print(f"Buz ({i})")
        buz.append(i)
    else:
        #print(i)
        pass
    i += 1

for osszeg in fizbuz:
    fizbuzSzamokOszzege = osszeg + fizbuzSzamokOszzege
for osszeg in buz:
    buzSzamokOszzege = osszeg + buzSzamokOszzege
for osszeg in fiz:
    fizSzamokOszzege = osszeg + fizSzamokOszzege


print(f"Fizbuz: {fizbuz}")
print(f"Fiz: {fiz}")
print(f"Buz: {buz}")
print(f"Ennyi fizbuz szám van: {len(fizbuz)}")
print(f"Ennyi fiz szám van: {len(fiz)}")
print(f"Ennyi buz szám van: {len(buz)}")
print(f"Fizbuz számok összege: {fizbuzSzamokOszzege}")
print(f"Fiz számok összege: {fizSzamokOszzege}")
print(f"Buz számok összege: {buzSzamokOszzege}")