from tkinter import *
import FestivalSQL
################## def's ##################

################## Hoofdprogramma ##################

window = Tk()
window.overrideredirect(True)
window.geometry("{0}x{1}+0+0".format(window.winfo_screenwidth(), window.winfo_screenheight()))
window.configure(bg="#DFDFDF")
#window.iconbitmap("MC_icon.ico") #Let op: Dit werkt niet op een MAC! Zet deze regel dan in commentaar
window.wm_title("Gedverderriedezepizasmaaktnaardrerrie Pizzeria")

closeWindow = Button(window, text="Close", width=50, height=2, bd=5, command=window.destroy)
closeWindow.grid(row=17,column=4)

window.mainloop()