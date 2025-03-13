from tkinter import *
import FestivalSQL

backgroundColor = "#DFDFDF"

################## def's ##################

################## Hoofdprogramma ##################

window = Tk()
window.overrideredirect(True)
window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))
window.configure(bg=backgroundColor)
#window.iconbitmap("MC_icon.ico") #Let op: Dit werkt niet op een MAC! Zet deze regel dan in commentaar
window.wm_title("Gedverderriedezepizasmaaktnaardrerrie Pizzeria")

spacer = Label(window, bg="orange", width=10, height= 10)
spacer.grid(row=1, column=0)

closeWindow = Button(window, text="Close", width=50, height=2, bd=5, command=window.destroy)
closeWindow.grid(row=2,column=2)



labelIntro = Label(window, text="Titel Festival!", width=200, height=2)
labelIntro.grid(row=0, column=1, sticky="W")

window.mainloop()