#dictionary
wechselkurse = {"EUR":1.0,
                "USD": 1.1,
                 "GBP": 0.85}

ausgangswährung = input("Von welcher Währung möchtest du umrechnen? (EUR, USD, GBP)")
zielwährung = input("In welche Währung möchtest du umwandeln? (EUR, USD, GBP)")
betrag = float(input("Welchen Betrag möchtest du umwandeln?"))

if ausgangswährung not in wechselkurse: print("Währung nicht erkannt")
if zielwährung not in wechselkurse: print("Währung nicht enthalten")

betrag_in_eur = betrag/wechselkurse[ausgangswährung]
ergebnis = betrag_in_eur * wechselkurse[zielwährung]

print(f"Der Kurs für deine Auswahl beträgt momentan {ergebnis}")