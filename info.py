# Fragt den Nutzer nach Name und Alter und gibt eine Antwort aus

name = input("Wie heißt du? ")
alter_text = input("Wie alt bist du? ")

# alter_text ist ein Text, wir wollen aber eine Zahl
alter = int(alter_text)

naechstes_jahr = alter + 1

print()
print(f"Hallo {name}!")
print(f"Du bist {alter} Jahre alt.")
print(f"Nächstes Jahr wirst du {naechstes_jahr} Jahre alt sein.")
