testsuly = float(input("Add meg a tömeged (kg): "))
magassag = float(input("Add meg a magasságod (cm): "))
magassagMeterben= magassag/100

bmi = testsuly/magassagMeterben**2

print(f'A BMI étrék: {round(bmi, 2)}')
if bmi <= 18.5:
    print("Alultáplált")
elif bmi  >= 18.5 and bmi < 24.9:
    print("Normális testsúly")
elif bmi  >= 25 and bmi < 29.9:
    print("Túlsúlyos ")
    
elif bmi  >= 30 and bmi < 34.9:
    print("Első fokú elhízás")
elif bmi  >= 35 and bmi < 39.9:
    print("Másodfokú elhízás (súlyos elhízás)")
else:
    print("Harmadfokú elhízás (nagyon súlyos elhízás)")
print("A BMI egyáltalán nem ad pontos képet az egyén testfelépítéséről.")
