from tkinter import *
from tkinter import font
from PIL import Image, ImageTk
import FestivalSQL

backgroundColor = "#A3A9AA"
fillColor = "#8D8E8E"
hoverColor = "#475B5A"
textColor = "black"
hoverTextColor = "white"

################## def's ##################
def on_enter(e): #e betekend in deze context any
    e.widget.config(bg=hoverColor, fg=hoverTextColor) #kleur veranderen wanneer je boven de knop hangt

def on_leave(e):
    e.widget.config(bg=fillColor, fg=textColor) #kleur terugveranderen

################## Hoofdprogramma ##################
window = Tk()
kopjesFont = font.Font(family="Arial", size= 24, weight="bold") #Best wel vet, ben erachter gekomen hoe ik text dik kan drukken.
titelFont = font.Font(family="Times New Roman", size= 100, weight="bold")
window.overrideredirect(True)
window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))
window.configure(bg=backgroundColor)
window.wm_title("PoePaaPop")

naastTitel = Label(window, bg=fillColor, bd=6, relief="solid", font=titelFont)
naastTitel.place(relwidth=1)
titel = Label(window, width= 20, bg=fillColor, text="P O E P A A P O P", bd=6, relief="solid", font=titelFont)
titel.place(x=156, y=0) #Ik gebruik hier place in plaats van grid omdat ik dit een logischere manier vind, en zo geen spacers hoef te gebruiken.



borderVert = Label(window, width=0, height=30, bg="black")
borderVert.place(x=206-50, y=205) #bij veel x waardes staat -50 omdat ik alles 50 naar links moest verplaatsen

borderHor = Label(window, height= 0, bg=backgroundColor, text= "______________", font=("Arial", 50)) #alle borders zijn puur omda ze er leuk uit zien
borderHor.place(x=236-50, y=250)

borderVert1 = Label(window, width=0, height=30, bg="black")
borderVert1.place(x=822-50, y=205)

borderHor1 = Label(window, height= 0, bg=backgroundColor, text= "______________", font=("Arial", 50))
borderHor1.place(x=236-50, y=450)

borderHor2 = Label(window, height= 0, bg=backgroundColor, text= "______________", font=("Arial", 50))
borderHor2.place(x=236-50, y=600)

borderHor3 = Label(window, height= 0, bg=backgroundColor, text= "_______________________", font=("Arial", 50))
borderHor3.place(x=925-50, y=450)

borderHor4 = Label(window, height= 0, bg=backgroundColor, text= "______________", font=("Arial", 50))
borderHor4.place(x=928-50, y=750)

borderHor5 = Label(window, height= 0, bg=backgroundColor, text= "-------------", font=("Arial", 50))
borderHor5.place(x=1515-50, y=400)

borderHor6 = Label(window, height= 0, bg=backgroundColor, text= "-------------", font=("Arial", 50))
borderHor6.place(x=1515-50, y=1000)

email = Label(window, text="Email:",bg=backgroundColor, font=kopjesFont)
email.place(x=236-50, y=200)
ingevoerde_email = StringVar()
invoerveldKlantnaam = Entry(window, textvariable=ingevoerde_email, bd=6, relief="solid", font=("Verdana", 18), bg=fillColor)
invoerveldKlantnaam.place(x=486-50, y=200)

phone = Label(window, text="Phone Number:",bg=backgroundColor, font=kopjesFont)
phone.place(x=236-50, y=250)
ingevoerde_telefoon = StringVar()
invoerveldtelefoon = Entry(window, textvariable=ingevoerde_telefoon, bd=6, relief="solid", font=("Verdana", 18), bg=fillColor)
invoerveldtelefoon.place(x=486-50, y=250)

name = Label(window, text="First Name:",bg=backgroundColor, font=kopjesFont)
name.place(x=236-50, y=350)
ingevoerde_voornaam = StringVar()
invoerveldVoornaam = Entry(window, textvariable=ingevoerde_voornaam, bd=6, relief="solid", font=("Verdana", 18), bg=fillColor)
invoerveldVoornaam.place(x=486-50, y=350)

prefix = Label(window, text="Prefix:",bg=backgroundColor, font=kopjesFont)
prefix.place(x=236-50, y=400)
ingevoerd_tussenvoegsel = StringVar()
invoerveldTussenvoegsel = Entry(window, textvariable=ingevoerd_tussenvoegsel, bd=6, relief="solid", font=("Verdana", 18), bg=fillColor)
invoerveldTussenvoegsel.place(x=486-50, y=400)

surname = Label(window, text="Surname:",bg=backgroundColor, font=kopjesFont)
surname.place(x=236-50, y=450)
ingevoerde_achternaam = StringVar()
invoerveldAchternaam = Entry(window, textvariable=ingevoerde_achternaam, bd=6, relief="solid", font=("Verdana", 18), bg=fillColor)
invoerveldAchternaam.place(x=486-50, y=450)

ZIPcode = Label(window, text="ZIP code:",bg=backgroundColor, font=kopjesFont)
ZIPcode.place(x=236-50, y=550)
ingevoerde_postcode = StringVar()
invoerveldPostcode = Entry(window, textvariable=ingevoerde_postcode, bd=6, relief="solid", font=("Verdana", 18), bg=fillColor)
invoerveldPostcode.place(x=486-50, y=550)

address = Label(window, text="Address:",bg=backgroundColor, font=kopjesFont)
address.place(x=236-50, y=600)
ingevoerd_adres = StringVar()
invoerveldAdres = Entry(window, textvariable=ingevoerd_adres, bd=6, relief="solid", font=("Verdana", 18), bg=fillColor)
invoerveldAdres.place(x=486-50, y=600)

selected = Label(window, text="Selected:",bg=backgroundColor, font=kopjesFont)
selected.place(x=1510-50, y=474)
listboxSelected = Listbox(window, height=10, width= 156, bd= 6, relief="solid", bg=fillColor)
listboxSelected.place(x=871-50, y=538)

confirm = Button(window, text="Confirm Selection", font=kopjesFont, bd=6, relief="solid", bg=fillColor, width= 15, height= 6)
confirm.place(x=1516-50, y=726)

campingSpot = Button(window, text="Camping Spot", font=kopjesFont, bd=6, relief="solid", bg=fillColor, width= 15)
campingSpot.place(x=1194-50, y=726)

parkingSpot = Button(window, text="Parking Spot", font=kopjesFont, bd=6, relief="solid", bg=fillColor, width= 15)
parkingSpot.place(x=871-50, y=726)

closeWindow = Button(window, text="Close", font=kopjesFont, bd=6, relief="solid", bg=fillColor, command=window.destroy, width= 15, height= 5)
closeWindow.place(x=1515-50, y=198)

weekend = Button(window, text="Weekend", font=kopjesFont, bd=6, relief="solid", bg=fillColor, width= 7, height= 5)
weekend.place(x=871-50, y=846)

friday = Button(window, text="Friday", font=kopjesFont, bd=6, relief="solid", bg=fillColor, width= 7, height= 5)
friday.place(x=1030-50, y=846)

saturday = Button(window, text="Saturday", font=kopjesFont, bd=6, relief="solid", bg=fillColor, width= 7, height= 5)
saturday.place(x=1189-50, y=846)

sunday = Button(window, text="Sunday", font=kopjesFont, bd=6, relief="solid", bg=fillColor, width=7, height= 5)
sunday.place(x=1346-50, y=846)

image1_path = r"images/Felix.png" #dit was me toch een gedoe om uit te vogelen haha
image1 = Image.open(image1_path)
image1 = image1.resize((610,355))
photo1 = ImageTk.PhotoImage(image1)

image_path = r"images/Aapop.png"  
image = Image.open(image_path)
image = image.resize((614, 300))  
photo = ImageTk.PhotoImage(image)

photoLabel = Label(window, image=photo, bd=6, relief="solid") #plaatje staat in een label
photoLabel.place(x=870-50, y=198)

photoLabel1 = Label(window, image=photo1, bd=6, relief="solid")
photoLabel1.place(x=206-50, y=700)

buttons = [
    confirm, closeWindow, weekend, friday, saturday, sunday, parkingSpot, campingSpot
]

for Button in buttons: #dit zorgt ervoor dat voor elke knop in de lijst buttons[] de knop aan on_enter() en on_leave() wordt gekoppeld
    Button.bind("<Enter>", on_enter) #run on_enter() als je over de knop hovert
    Button.bind("<Leave>", on_leave) #run on_leave() als je weer van de knop af gaat

window.mainloop()