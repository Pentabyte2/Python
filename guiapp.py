## https://www.geeksforgeeks.org/python-tkinter-checkbutton-widget/

from tkinter import *                                                               ## Modul importieren
from tkinter.ttk import *                                                           ## Modul importieren

root = Tk()                                                                         ## Root(fenster) erstellen
root.title("APP_NAME_HERE")                                                         ## Fenstertitel
root.geometry('600x600')                                                            ## Auflösung
label = Label(root, text ="Label Text").pack()                                      ## Text (plain)

frame = Frame(root)                                                                 ## Rahmen
frame.pack()                                                                        ## Geometrie Rahmen (Manager nach Reihen und Zeilen/Standarteinstellungen)

botframe = Frame(root)                                                              ## Rahmen
botframe.pack(side=BOTTOM)                                                          ## Geometrie (Einstellung auf pos Boden)


buttonl = Button(frame,text='Button Left')                                          ## Knopf ohne Funktion
buttonl.pack(side=LEFT)                                                             ## Geometrie    

buttonm = Button(frame, text='Button Mid')                                          ## Knopf ohne Funktion
buttonm.pack(side=LEFT)                                                             ## Geometrie    

buttonr = Button(frame, text='Button Right')                                        ## Knopf ohne Funktion
buttonr.pack(side=LEFT)                                                             ## Geometrie    

user_name = Label(text='Username').place(x = 100, y= 200)                           ## Text mit x,y Position
user_password = Label(text='Password').place(x = 100, y = 240)                      ## Text mit x,y Position
user_name_input_area = Entry(width=50).place(x = 200, y = 200)                      ## Eingabefeld mit x,y Position
user_password_input_area = Entry(width=50).place(x = 200, y = 240)                  ## Eingabefeld mit x,y Position

submit_button = Button(root, text='Submit').place(x = 100, y = 300)                 ## 'Submit' Button im root mit x,y Position


buttonquit = Button(botframe, text="Quit", command= root.destroy)                   ## Knopf mit Funktion (Zerstört Root Fenster)
buttonquit.pack()                                                                   ## Geometrie (mit Anordnung)     

rad = Tk()                                                                          ## Komplett neues Fenster
rad.geometry('200x200')                                                             ## Auflösung vom Fenster 'rad'

v = StringVar(rad, '1')                                                             ## Speichert alles

values = {"RadioButton 1" : "1",                                                    ## Werte für die Namen
        "RadioButton 2" : "2",
        "RadioButton 3" : "3",
        "RadioButton 4" : "4",
        "RadioButton 5" : "5"}

for (text, value) in values.items():                                                ## Schleifen für die Automatische RadioButton Erstellung
    Radiobutton(rad, text = text, variable = v,
        value = value).pack(side = TOP, ipady = 5)

mainloop()                                                                          ## Loop für alle Fenster (geändert von root.mainloop() zu mainloop(), da
                                                                                    ## neues parralel laufendes Fenster)
