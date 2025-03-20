# hey renske dit het PO van Manèl en Chiel

import sqlite3
with sqlite3.connect("Festival.db") as db:
    cursor = db.cursor()#cursor is object waarmee je data uit de database kan halen

################## def's ##################

def maakTabellenAan():
     # Maak een nieuwe tabel met 5 kolommen
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
 print("Tabel 'tbl_NAW' aangemaakt.") 
 cursor.execute("""
 CREATE TABLE IF NOT EXISTS tbl_programma(
 programmaID INTERGER PRIMARY KEY NOT NULL,
 dag TEXT NOT NULL,
 hoofdartiest TEXT NOY NULL,
 begintijd TIME NOT NULL);""")
 print("Tabel 'tbl_winkelWagen' aangemaakt.")

def printTabel(tabel_naam):
    cursor.execute("SELECT * FROM " + tabel_naam) #SQL om ALLE gegevens te halen
    opgehaalde_gegevens = cursor.fetchall() #sla gegevens op in een variabele
    print("Tabel " + tabel_naam + ":", opgehaalde_gegevens) #druk gegevens a

def voegNAWToe(ingevoerd_voornaam, ingevoerd_tussenvoegsel, ingevoerd_achternaam, ingevoerd_postcode,ingevoerd_adres, ingevoerd_email, ingevoerd_telefoon ):
    cursor.execute("INSERT INTO tbl_NAW VALUES(null, ?, ?, ?, ?, ?, ?, ?)", (ingevoerd_voornaam, ingevoerd_tussenvoegsel, ingevoerd_achternaam,ingevoerd_postcode,ingevoerd_adres, ingevoerd_email,ingevoerd_telefoon ))
    db.commit()
    print("Klant toegevoegd:")
    printTabel("tbl_NAW")
    
def tabel_klanten():
 cursor.execute("SELECT * FROM tbl_klanten")
 resultaat = cursor.fetchall()
 print("Tabel tbl_klanten:", resultaat)
 return resultaat
################## Hoofdprogramma ##################

