# hey renske dit het PO van Manèl en Chiel

import sqlite3
with sqlite3.connect("MCPizzeria.db") as db:
    cursor = db.cursor()#cursor is object waarmee je data uit de database kan halen

################## def's ##################

def maakTabellenAan():
     # Maak een nieuwe tabel met 3 kolommen: id, naam, prijs
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tbl_klanten(
            gerechtID INTEGER PRIMARY KEY AUTOINCREMENT,
            gerechtNaam TEXT NOT NULL,
            gerechtPrijs REAL NOT NULL);""")
    
    print("Tabel 'tbl_klanten' aangemaakt.")
################## Hoofdprogramma ##################