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

def zoekpizza():
    gevonden_pizza = MCPizzeriaSQL.zoekPizzaInTabel(invoerveldpizzanaam.get())
    print(gevonden_pizza) # om te testen
    invoerveldpizzanaam.delete(0, END) #invoerveld voor naam leeg maken
    for rij in gevonden_pizza: #voor elke rij dat de query oplevert
        invoerveldpizzanaam.insert(END, rij[1]) 

def toonMenuInListbox():
 listboxMenu.delete(1, END) #maak de listbox leeg
 pizza_tabel = MCPizzeriaSQL.vraagOpGegevensPizzaTabel()
 for regel in pizza_tabel:
  listboxMenu.insert(END, regel) #voeg elke regel uit resultaat in
### functie voor het selecteren van een rij uit de listbox en deze in een andere veld te plaatsen
def haalGeselecteerdeRijOp(event):
 #bepaal op welke regel er geklikt is
 geselecteerdeRegelInLijst = listboxMenu.curselection()[0] 
 #haal tekst uit die regel
 geselecteerdeTekst = listboxMenu.get(geselecteerdeRegelInLijst) 
 #verwijder tekst uit veld waar je in wilt schrijven, voor het geval er al iets staat
 invoerveldGeselecteerdePizza.delete(0, END) 
 #zet tekst in veld
 invoerveldGeselecteerdePizza.insert(0, geselecteerdeTekst)  
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
knopzoekopklantnaam.grid(row=1, column=6)

labelIntro = Label(window, text="Klantnummer:")
labelIntro.grid(row=2, column=0, sticky="W")
invoerveldKlantNr = Entry(window)
invoerveldKlantNr.grid(row=2, column=1, sticky="W")

labelIntro = Label(window, text="pizzanaam:")
labelIntro.grid(row=3, column=0, sticky="W")
ingevoerde_pizza = StringVar()
invoerveldpizzanaam = Entry(window, textvariable=ingevoerde_pizza)
invoerveldpizzanaam.grid(row=3, column=1, sticky="W")
knopzoekopklantnaam = Button(window, text="Zoek pizza", width=12, command=zoekpizza)
knopzoekopklantnaam.grid(row=3, column=6)

labelIntro = Label(window, text="Mogelijkheden:")
labelIntro.grid(row=4, column=0, sticky="W")
listboxMenu = Listbox(window, height=6, width=50)
listboxMenu.grid(row=4, column=1, rowspan=6, columnspan=6, sticky="W")
listboxMenu.insert(0, "ID Gerecht Prijs")
listboxMenu.bind('<<ListboxSelect>>', haalGeselecteerdeRijOp)
knopToonPizzas = Button(window, text="Toon alle pizzas", width=12, command=toonMenuInListbox)
knopToonPizzas.grid(row=4, column=6)

labelIntro = Label(window, text="Gekozen pizza:")
labelIntro.grid(row=11, column=0, sticky="W")
invoerveldGeselecteerdePizza = Entry(window)
invoerveldGeselecteerdePizza.grid(row=11, column=1, sticky="W")

Voegtoeknop = Button(window, text="Voeg toe", width=12)
Voegtoeknop.grid(row=12, column=6)
aantalGekozen = IntVar()
aantalGekozen.set(1)


#reageert op gebruikersinvoer, deze regel als laatste laten staan
window.mainloop()