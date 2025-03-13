# hey renske dit het PO van Manèl en Chiel

import sqlite3
with sqlite3.connect("Festival.db") as db:
    cursor = db.cursor()#cursor is object waarmee je data uit de database kan halen

################## def's ##################

def maakTabellenAan():
     # Maak een nieuwe tabel met 3 kolommen: id, naam, prijs
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tbl_klanten(
            gegrevensID INTEGER PRIMARY KEY AUTOINCREMENT,
            consumentID INTEGER  NOT NULL,
            programmaID INTEGER NOT NULL,
            campingplaats INTEGER,
            pakeerplek INTEGER);""")
    
    print("Tabel 'tbl_klanten' aangemaakt.")

def maaknieuwetabbellenaan():
 cursor.execute("""
 CREATE TABLE IF NOT EXISTS tbl_NAW(
 consumentID INTEGER PRIMARY KEY AUTOINCREMENT,
 voornaam TEXT NOT NULL,
 tussenvoegsel TEXT,
 achternaam TEXT NOT NULL,
 );""")
 print("Tabel 'tbl_klanten' aangemaakt.") 
 cursor.execute("""
 DESTROY TABLE IF EXIST tbl_winkelWagen
 CREATE TABLE IF NOT EXISTS tbl_winkelWagen(
 bestelRegel INTEGER PRIMARY KEY AUTOINCREMENT,
 klantNr INTEGER,
 gerechtID INTEGER,
 aantal INTEGER NOT NULL,
 FOREIGN KEY (klantNr) REFERENCES tbl_klanten(klantNr)
 FOREIGN KEY (gerechtID) REFERENCES tbl_pizzas(gerechtID));""")
print("Tabel 'tbl_winkelWagen' aangemaakt.")
################## Hoofdprogramma ##################
maakTabellenAan()