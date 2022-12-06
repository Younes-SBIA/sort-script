"""
Trier les fichiers contenus dans le dossier data selon les associations suivantes :
mp3, wav, flac : Musique
avi, mp4, gif : Videos
bmp, png, jpg : Images
txt, pptx, csv, xls, odp, pages,ttf,pdf,epub : Documents
zip, rar, Compressed
exe, Programs
autres : Divers
"""

from pathlib import Path


EXTENSIONS_MAPPING = {
    ".mp3": "Musique",
    ".wav": "Musique",
    ".mp4": "Videos",
    ".avi": "Videos",
    ".gif": "Videos",
    ".bmp": "Images",
    ".png": "Images",
    ".jpg": "Images",
    ".tif": "Images",
    ".txt": "Documents",
    ".pptx": "Documents",
    ".csv": "Documents",
    ".xls": "Documents",
    ".odp": "Documents",
    ".pages": "Documents",
    ".ttf": "Documents",
    ".pdf": "Documents",
    ".epub": "Documents",
    ".zip": "Compressed",
    ".rar": "Compressed",
    ".gz": "Compressed",
    ".exe": "Programs", }

BASE_DIR = Path.home() / "Downloads"

# On récupère tous les fichiers dans le dossier de base
files = [f for f in BASE_DIR.iterdir() if f.is_file()]

for file in files:  # On boucle sur chaque fichier

    # On récupère le dossier cible à partir du dictionnaire
    dossier_cible = EXTENSIONS_MAPPING.get(file.suffix, "Divers")
    # On concatène le dossier de base avec le dossier cible
    dossier_cible_absolu = BASE_DIR / dossier_cible
    # On crée le dossier cible s'il n'existe pas déjà
    dossier_cible_absolu.mkdir(exist_ok=True)
    # On concatène le dossier cible avec le nom du fichier
    fichier_cible = dossier_cible_absolu / file.name
    # On déplace le fichier
    file.rename(fichier_cible)
