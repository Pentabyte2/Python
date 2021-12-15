## https://www.geeksforgeeks.org/python-tkinter-checkbutton-widget/

from tkinter import * 
from tkinter.ttk import *

root = Tk()                                                                         ## Root(fenster) erstellen
root.title("APP_NAME_HERE")                                                         ## Fenstertitel
root.geometry('600x600')                                                            ## Auflösung
label = Label(root, text ="Label Text").pack()                                      ## Text (plain)

frame = Frame(root)                                                                 ## Rahmen
frame.pack()                                                                        ## Geometrie (Manager nach Reihen und Zeilen)

botframe = Frame(root)                                                              
botframe.pack(side=BOTTOM)


buttonl = Button(frame,text='Button Left')                                          ## Knopf ohne Funktion
buttonl.pack(side=LEFT)                                                             ## Geometrie    

buttonm = Button(frame, text='Button Mid')                                          ## Knopf ohne Funktion
buttonm.pack(side=LEFT)                                                             ## Geometrie    

buttonr = Button(frame, text='Button Right')                                        ## Knopf ohne Funktion
buttonr.pack(side=LEFT)                                                             ## Geometrie    

user_name = Label(text='Username').place(x = 100, y= 200)
user_password = Label(text='Password').place(x = 100, y = 240)
user_name_input_area = Entry(width=50).place(x = 200, y = 200)
user_password_input_area = Entry(width=50).place(x = 200, y = 240)

submit_button = Button(root, text='Submit').place(x = 100, y = 300)


buttonquit = Button(botframe, text="Quit", command= root.destroy)                   ## Knopf mit Funktion (Zerstört Root Fenster)
buttonquit.pack()                                                                   ## Geometrie (mit Anordnung)     

rad = Tk()
rad.geometry('200x200')

v = StringVar(rad, '1')

values = {"RadioButton 1" : "1",
        "RadioButton 2" : "2",
        "RadioButton 3" : "3",
        "RadioButton 4" : "4",
        "RadioButton 5" : "5"}

for (text, value) in values.items():
    Radiobutton(rad, text = text, variable = v,
        value = value).pack(side = TOP, ipady = 5)

mainloop()