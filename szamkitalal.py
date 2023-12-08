import random

alsoHatar = int(input("Mi legyen a lehető legkisebb szám: "))
felsoHatar = int(input("Mi legyen a lehető legnagyobb szám: "))



probalkozasSzam = int(input("Mennyi legyen a max próbálkozás? "))
gondoltSzam = random.randint(alsoHatar, felsoHatar)
probalkozasok = 1
while True:
    tippeltSzam = int(input(f"Adj meg egy számot {alsoHatar} és {felsoHatar} között: "))
    if tippeltSzam > gondoltSzam:
        print("A gondolt szám kisebb")
    elif tippeltSzam < gondoltSzam:
        print("A gondolt szám nagyobb")
    elif tippeltSzam == gondoltSzam:
        print("Gratulálok! Eltaláltad a gondolt számot.")
        print(f'Próbálkozások: {probalkozasok}')
        break
    
    if probalkozasok >=probalkozasSzam:
        print(f"Nincs több próbálkozásod. A gondolt szám {gondoltSzam} volt.")
        break
    if tippeltSzam < alsoHatar or tippeltSzam> felsoHatar:
        print(f"{alsoHatar} és {felsoHatar} között adj meg egy számot.")
    probalkozasok+=1
print("Vége a játéknak.")
