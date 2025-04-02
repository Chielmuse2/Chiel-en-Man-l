# hey renske dit het PO van Manèl en Chiel

import random
import sqlite3
with sqlite3.connect("Festival.db") as db:
    cursor = db.cursor()#cursor is object waarmee je data uit de database kan halen

################## def's ##################

def maakTabellenAan():
     # Maak een nieuwe tabel met 5 kolommen
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tbl_klant(
            gegrevensID INTEGER PRIMARY KEY AUTOINCREMENT,
            consumentID INTEGER NOT NULL,
            programmaID INTEGER,
            campingplaats INTEGER,
            pakeerplek INTEGER,
            FOREIGN KEY (consumentID) REFERENCES tbl_NAW(consumentID),
            FOREIGN KEY (programmaID) REFERENCES tbl_programma(programmaID));""")
    
    print("Tabel 'tbl_klant' aangemaakt.")

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
 programmaID INTEGER PRIMARY KEY NOT NULL,
 dag TEXT NOT NULL,
 hoofdartiest TEXT NOT NULL,
 begintijd TIME NOT NULL);""")
 print("Tabel 'tbl_programma' aangemaakt.")

def vulprogramma():
 cursor.execute("INSERT INTO tbl_programma (programmaID, dag, hoofdartiest, begintijd) VALUES (1, 'Vrijdag', 'J. Bernhardt', '16:00:00')")
 cursor.execute("INSERT INTO tbl_programma (programmaID, dag, hoofdartiest, begintijd) VALUES (2, 'Zaterdag', 'Franz Ferdinand', '12:00:00')")
 cursor.execute("INSERT INTO tbl_programma (programmaID, dag, hoofdartiest, begintijd) VALUES (3, 'Zondag', 'Muse', '12:00:00')")
 cursor.execute("INSERT INTO tbl_programma (programmaID, dag, hoofdartiest, begintijd) VALUES (4, 'Weekend', 'J. Bernhardt, Franz Ferdinand en Muse', '16:00:00')")
 db.commit()
 printTabel("tbl_programma")

def verwijderNAW(NUMMER):
    cursor.execute("DELETE FROM tbl_NAW WHERE consumentID = ?", (NUMMER,))
    print("Gerecht verwijderd uit 'tbl_NAW':", NUMMER )
    db.commit() #gegevens naar de database wegschrijven
    printTabel("tbl_NAW")

def printTabel(tabel_naam):
    cursor.execute("SELECT * FROM " + tabel_naam) #SQL om ALLE gegevens te halen
    opgehaalde_gegevens = cursor.fetchall() #sla gegevens op in een variabele
    print("Tabel " + tabel_naam + ":", opgehaalde_gegevens) #druk gegevens a

def voegNAWToe(ingevoerd_voornaam, ingevoerd_tussenvoegsel, ingevoerd_achternaam, ingevoerd_postcode,ingevoerd_adres, ingevoerd_email, ingevoerd_telefoon ):
 cursor.execute("SELECT consumentID FROM tbl_NAW WHERE voornaam = ?", (ingevoerd_voornaam,))
 zoek = cursor.fetchone()
 print(zoek)
 if zoek == None:
    cursor.execute("INSERT INTO tbl_NAW VALUES(null, ?, ?, ?, ?, ?, ?, ?)", (ingevoerd_voornaam, ingevoerd_tussenvoegsel, ingevoerd_achternaam,ingevoerd_postcode,ingevoerd_adres, ingevoerd_email,ingevoerd_telefoon ))
    db.commit()
    print("Klant toegevoegd:")
    printTabel("tbl_NAW")
 else:
  print("klant bestaat al")
   
    
def tabel_klanten(ingevoerde_voornaam):
 cursor.execute( """
    SELECT  tbl_NAW.voornaam,
            tbl_NAW.tussenvoegsel,
            tbl_NAW.achternaam,
            tbl_programma.dag,
            tbl_programma.hoofdartiest,
            tbl_programma.begintijd,
            tbl_klant.campingplaats,
            tbl_klant.pakeerplek
    FROM tbl_klant 
        LEFT JOIN tbl_NAW ON tbl_klant.consumentID = tbl_NAW.consumentID 
        LEFT JOIN tbl_programma ON tbl_klant.programmaID = tbl_programma.programmaID
    WHERE tbl_NAW.voornaam = ?; """, (ingevoerde_voornaam,))
 resultaat = cursor.fetchall()
 print("Tabel list:", resultaat)
 return resultaat

def knopvrijdag(ingevoerde_voornaam):
 dag = 1
 cursor.execute("SELECT consumentID FROM tbl_NAW WHERE voornaam = ?", (ingevoerde_voornaam,))
 klant = cursor.fetchone()
 print(klant)
 cursor.execute("SELECT consumentID FROM tbl_klant WHERE consumentID = ?",(klant[0],))
 zoek = cursor.fetchone()
 print(zoek)
 if zoek == None:
    cursor.execute("INSERT INTO tbl_klant VALUES(null, ?,?,?,?)", (klant[0],dag,None,None))
    db.commit()
     #gegevens naar de database wegschrijven
    print("made")
 else:
    cursor.execute("UPDATE tbl_klant SET programmaID = ? WHERE consumentID = ?", (dag, klant[0]))
    db.commit()
    print("updated")
 print("programma aangepast")
 printTabel("tbl_klant")

def knopzaterdag(ingevoerde_voornaam):
 dag = 2
 cursor.execute("SELECT consumentID FROM tbl_NAW WHERE voornaam = ?", (ingevoerde_voornaam,))
 klant = cursor.fetchone()
 print(klant)
 cursor.execute("SELECT consumentID FROM tbl_klant WHERE consumentID = ?",(klant[0],))
 zoek = cursor.fetchone()
 print(zoek)
 if zoek == None:
    cursor.execute("INSERT INTO tbl_klant VALUES(null, ?,?,?,?)", (klant[0],dag,None,None))
    db.commit()
     #gegevens naar de database wegschrijven
    print("made")
 else:
    cursor.execute("UPDATE tbl_klant SET programmaID = ? WHERE consumentID = ?", (dag, klant[0]))
    db.commit()
    print("updated")
 print("programma aangepast")
 printTabel("tbl_klant")

def knopzondag(ingevoerde_voornaam):
 dag = 3
 cursor.execute("SELECT consumentID FROM tbl_NAW WHERE voornaam = ?", (ingevoerde_voornaam,))
 klant = cursor.fetchone()
 print(klant)
 cursor.execute("SELECT consumentID FROM tbl_klant WHERE consumentID = ?",(klant[0],))
 zoek = cursor.fetchone()
 print(zoek)
 if zoek == None:
    cursor.execute("INSERT INTO tbl_klant VALUES(null, ?,?,?,?)", (klant[0],dag,None,None))
    db.commit()
     #gegevens naar de database wegschrijven
    print("made")
 else:
    cursor.execute("UPDATE tbl_klant SET programmaID = ? WHERE consumentID = ?", (dag, klant[0]))
    db.commit()
    print("updated")
 print("programma aangepast")
 printTabel("tbl_klant")

def knopweekend(ingevoerde_voornaam):
 dag = 4
 cursor.execute("SELECT consumentID FROM tbl_NAW WHERE voornaam = ?", (ingevoerde_voornaam,))
 klant = cursor.fetchone()
 print(klant)
 cursor.execute("SELECT consumentID FROM tbl_klant WHERE consumentID = ?",(klant[0],))
 zoek = cursor.fetchone()
 print(zoek)
 if zoek == None:
    cursor.execute("INSERT INTO tbl_klant VALUES(null, ?,?,?,?)", (klant[0],dag,None,None))
    db.commit()
     #gegevens naar de database wegschrijven
    print("made")
 else:
    cursor.execute("UPDATE tbl_klant SET programmaID = ? WHERE consumentID = ?", (dag, klant[0]))
    db.commit()
    print("updated")
 print("programma aangepast")
 printTabel("tbl_klant")

def knopcampingplek(ingevoerde_voornaam):
 campingplek = random.randint(100,450)
 cursor.execute("SELECT consumentID FROM tbl_NAW WHERE voornaam = ?", (ingevoerde_voornaam,))
 klant = cursor.fetchone()
 print(klant)
 cursor.execute("SELECT consumentID FROM tbl_klant WHERE consumentID = ?",(klant[0],))
 zoek = cursor.fetchone()
 print(zoek)
 if zoek == None:
    cursor.execute("INSERT INTO tbl_klant VALUES(null, ?,?,?,?)", (klant[0],None,campingplek,None))
    db.commit()
     #gegevens naar de database wegschrijven
    print("made")
 else:
    cursor.execute("UPDATE tbl_klant SET campingplaats = ? WHERE consumentID = ?", (campingplek, klant[0]))
    db.commit()
    print("updated")
 print("programma aangepast")
 printTabel("tbl_klant")

def knopparkeerplek(ingevoerde_voornaam):
 parkeerplek = random.randint(10,4500)
 cursor.execute("SELECT consumentID FROM tbl_NAW WHERE voornaam = ?", (ingevoerde_voornaam,))
 klant = cursor.fetchone()
 print(klant)
 cursor.execute("SELECT consumentID FROM tbl_klant WHERE consumentID = ?",(klant[0],))
 zoek = cursor.fetchone()
 print(zoek)
 if zoek == None:
    cursor.execute("INSERT INTO tbl_klant VALUES(null, ?,?,?,?)", (klant[0],None,None,parkeerplek))
    db.commit()
     #gegevens naar de database wegschrijven
    print("made")
 else:
    cursor.execute("UPDATE tbl_klant SET pakeerplek = ? WHERE consumentID = ?", (parkeerplek, klant[0]))
    db.commit()
    #gegevens naar de database wegschrijven
    print("updated")
 print("programma aangepast")
 printTabel("tbl_klant")
################## Hoofdprogramma ##################

