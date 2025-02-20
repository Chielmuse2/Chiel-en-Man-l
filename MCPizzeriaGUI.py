# Dit bestand zorgt voor de gebruikersinterface (GUI)van onze programma.
# Vul hier de naam van je programma in:
#
#
# Vul hier jullie namen in:
# BroSmarenDeDronestriker
# tjiel
#
#
#


### --------- Bibliotheken en globale variabelen -----------------
from tkinter import *
import MCPizzeriaSQL


### ---------  Functie definities  -----------------
def zoekKlant():
 #haal de ingevoerde_klantnaam op uit het invoerveld
 # en gebruik dit om met SQL de klant in database te vinden
 gevonden_klanten = MCPizzeriaSQL.zoekKlantInTabel(invoerveldKlantnaam.get())
 print(gevonden_klanten) # om te testen
 invoerveldKlantnaam.delete(0, END) #invoerveld voor naam leeg maken
 invoerveldKlantNr.delete(0, END) #invoerveld voor klantNr leeg maken
 for rij in gevonden_klanten: #voor elke rij dat de query oplevert
    #toon klantnummer, de eerste kolom uit het resultaat in de invoerveld
    invoerveldKlantNr.insert(END, rij[0]) 
    #toon klantAchternaam, de tweede kolom uit het resultaat in de invoerveld
    invoerveldKlantnaam.insert(END, rij[1]) 

### --------- Hoofdprogramma  ---------------

window = Tk()
window.iconbitmap("MC_icon.ico") #Let op: Dit werkt niet op een MAC! Zet deze regel dan in commentaar
window.wm_title("Gedverderriedezepizasmaaktnaardrerrie Pizzeria")

closeWindow = Button(window, text="Close", width=50, height=2, command=window.destroy)
closeWindow.grid(row=17,column=4)
labelIntro = Label(window, text="HALLOOOOOOOO!")
labelIntro.grid(row=0, column=0, sticky="W")

labelIntro = Label(window, text="Klantnaam:")
labelIntro.grid(row=1, column=0, sticky="W")
ingevoerde_klantnaam = StringVar()
invoerveldKlantnaam = Entry(window, textvariable=ingevoerde_klantnaam)
invoerveldKlantnaam.grid(row=1, column=1, sticky="W")
knopzoekopklantnaam = Button(window, text="Zoek klant", width=12, command=zoekKlant)
knopzoekopklantnaam.grid(row=1, column=4)

labelIntro = Label(window, text="Klantnummer:")
labelIntro.grid(row=2, column=0, sticky="W")
invoerveldKlantNr = Entry(window)
invoerveldKlantNr.grid(row=2, column=1, sticky="W")

labelIntro = Label(window, text="pizzanaam:")
labelIntro.grid(row=3, column=0, sticky="W")
ingevoerde_pizzanaam = StringVar()
invoerveldpizzanaam = Entry(window, textvariable=ingevoerde_pizzanaam)
invoerveldpizzanaam.grid(row=3, column=1, sticky="W")

labelIntro = Label(window, text="Mogelijkheden:")
labelIntro.grid(row=4, column=0, sticky="W")
#reageert op gebruikersinvoer, deze regel als laatste laten staan
window.mainloop()