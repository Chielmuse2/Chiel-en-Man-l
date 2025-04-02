# hey renske dit het PO van Manèl en Chiel

import sqlite3
with sqlite3.connect("Festival.db") as db:
    cursor = db.cursor()#cursor is object waarmee je data uit de database kan halen

################## def's ##################

def maaktabel():
    cursor.execute("CREATE TABLE IF NOT EXISTS tbl_consument (gegvensID INTEGER PRIMARY KEY AUTOINCREMENT, consumentID INTERGER NOT NULL, programmaID INTERGER NOT NULL, dag_kamping INTERGER, parkeerplek INTERGER)")
    print("tabel 'tbl_consument' aangemaakt")

def printtabel(tabel_naam):
 cursor.execute("SELECT * FROM " + tabel_naam) #SQL om ALLE gegevens te halen
 opgehaalde_gegevens = cursor.fetchall() #sla gegevens op in een variabele
 print("Tabel " + tabel_naam + ":", opgehaalde_gegevens) #druk gegevens af
################## Hoofdprogramma ##################
maaktabel()
printtabel("tbl_consument")