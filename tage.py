name_text = input("Wie heisst du? ")

alter_text = input("Wie alt bist du? ")
alter = int(alter_text)

tage = alter * 365

print(f"{name_text}, du hast ungefaer {tage} Tage gelebt.")