groesse_text = input("Bitte gebe deine Groesse in cm an.")
gewicht_text = input("Wie viel wiegst du momentan?")
groesse = float(groesse_text)
gewicht = float(gewicht_text)
groesse_m = groesse/100

bmi = gewicht/(groesse_m)**2
bmi_gerundet = round(bmi, 1)

if bmi < 18.5: print("Du solltest wirklich mehr essen Kollege")
elif bmi < 25: print("Dein Essverhalten scheint top zu sein")
elif bmi < 30: print("Du solltest anfangen abzunehmen Kollege")
else: print("Du bist echt mies fett du elender Pommespanzer")

print(f"Dein Wert ist naemlich {bmi_gerundet}")