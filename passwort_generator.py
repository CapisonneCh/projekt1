import random
laenge_text = input("Wie lang soll das Passwort sein? ")
laenge = int(laenge_text)
klein = "abcdefghijklmnopqrstuvwxyz"
gross = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
zahlen = "0123456789"
sonder = "!@#$%&*?"
alle_zeichen = klein + gross + zahlen + sonder

passwort = ""

for i in range(laenge):
    zufalls_zeichen = random.choice(alle_zeichen)
    passwort = passwort + zufalls_zeichen

print(f"Dein neues Passwort lautet: {passwort}")