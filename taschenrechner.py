zahl1_text = input("Der Taschenrechner ist sehr einfach und kann nur 2 Zahlen eingeben. Bitte gebe die erste Zahl ein.")
zahl2_text = input("Bitte gebe nun die zweite Zahl ein")
zahl1 = float(zahl1_text)
zahl2 = float(zahl2_text)

operation = input("Welche Operation möchtest du verwenden (+ - * /)")

if operation == "+": ergebnis = zahl1 + zahl2
elif operation == "-": ergebnis = zahl1 - zahl2
elif operation == "*": ergebnis =zahl1 * zahl2
elif operation == "/":
    if zahl2==0: print("Division mit 0 versucht -> ungültig")
    else: ergebnis = zahl1/zahl2
else: print("Fehler bei Operationsauswahl")

print(f"Ergebnis: {ergebnis}")