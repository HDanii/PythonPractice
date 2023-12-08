felsoHatar= int(input("Kérem a sorozat alsó határát: "))
alsoHatar= int(input("Kérem a sorozat felső határát: "))
osszeg=0
while felsoHatar<=alsoHatar:
    osszeg+=felsoHatar
    felsoHatar+=1
print(f'Az összeg: {osszeg}')
