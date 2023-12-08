szam = int(input("Adj meg egy számot: "))
lepesek = 0
while szam > 1:
    
    if szam % 2 == 0:
        szam = int(szam/2)
        lepesek += 1
    else:
        szam = int((szam*3) + 1)
        lepesek += 1
    print(szam)
    

print(f"A lépések száma: {lepesek}")





