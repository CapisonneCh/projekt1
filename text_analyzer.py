text = input("Gib deinen Text ein ")

anzahl_zeichen=len(text)

woerter_liste= text.split()
anzahl_woerter = len(woerter_liste)

text_klein = text.lower()
anzahl_e = text_klein.count("e")

print(f"Der Text hat {anzahl_zeichen} Zeichen")
print(f"Der Text hat {anzahl_woerter} Wörter")
print(f"Der Buchstabe e kommt {anzahl_e} Mal vor")