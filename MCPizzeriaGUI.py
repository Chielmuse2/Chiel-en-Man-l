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


### --------- Hoofdprogramma  ---------------

window = Tk()
window.iconbitmap("MC_icon.ico") #Let op: Dit werkt niet op een MAC! Zet deze regel dan in commentaar
window.wm_title("Gedverderriedezepizasmaaktnaardrerrie Pizzeria")

closeWindow = Button(window, text="Close", width=50, height=2, command=window.destroy)
closeWindow.grid(row=17,column=4)
labelIntro = Label(window, text="HALLOOOOOOOO!")
labelIntro.grid(row=0, column=0, sticky="W")

#reageert op gebruikersinvoer, deze regel als laatste laten staan
window.mainloop()