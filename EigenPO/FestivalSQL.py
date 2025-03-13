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
            consumentID INTEGER NOT NULL,
            programmaID INTEGER NOT NULL,
            campingplaats INTEGER,
            pakeerplek INTEGER,
            FOREIGN KEY (consumentID) REFERENCES tbl_NAW(consumentID),
            FOREIGN KEY (programmaID) REFERENCES tbl_programma(programmaID));""")
    
    print("Tabel 'tbl_klanten' aangemaakt.")

def maaknieuwetabbellenaan():
 cursor.execute("""
 CREATE TABLE IF NOT EXISTS tbl_NAW(
 consumentID INTEGER PRIMARY KEY AUTOINCREMENT,
 voornaam TEXT NOT NULL,
 tussenvoegsel TEXT,
 achternaam TEXT NOT NULL,
 postcode TEXT NOT NULL,
 adres TEXT NOT NULL,
 email TEXT NOT NULL,
 telefoonnummer TEXT);""")
 print("Tabel 'tbl_klanten' aangemaakt.") 
 cursor.execute("""
 CREATE TABLE IF NOT EXISTS tbl_programma(
 programmaID INTERGER PRIMARY KEY NOT NULL,
 dag TEXT NOT NULL,
 hoofdartiest TEXT NOY NULL,
 begintijd TIME NOT NULL);""")
 print("Tabel 'tbl_winkelWagen' aangemaakt.")

################## Hoofdprogramma ##################

