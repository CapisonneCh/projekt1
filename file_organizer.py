import os
import shutil

basis_ordner = "testordner"

dateitypen = {
    "Bilder": [".jpg", ".png"],
    "Dokumente": [".pdf", ".docx", ".txt", ".md"],
    "Audio": [".mp3"],
    "Video": [".mp4"],
    "Archive": [".zip"]
}

# Zielordner erstellen
for ordnername in dateitypen:
    ziel = os.path.join(basis_ordner, ordnername)
    if not os.path.exists(ziel):
        os.makedirs(ziel)

# Dateien sortieren
for dateiname in os.listdir(basis_ordner):
    pfad = os.path.join(basis_ordner, dateiname)

    # Ordner überspringen
    if os.path.isdir(pfad):
        continue

    _, endung = os.path.splitext(dateiname)

    verschoben = False

    for ordnername, endungen in dateitypen.items():
        if endung in endungen:
            neuer_pfad = os.path.join(basis_ordner, ordnername, dateiname)
            shutil.move(pfad, neuer_pfad)
            verschoben = True
            break

    if not verschoben:
        sonst = os.path.join(basis_ordner, "Sonstiges")
        if not os.path.exists(sonst):
            os.makedirs(sonst)
        shutil.move(pfad, os.path.join(sonst, dateiname))
