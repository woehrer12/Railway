#!/usr/bin/python
#-*- coding:utf-8 -*-

#from tkinter import *
import tkinter as tk
from tkinter import messagebox, filedialog
from Tkinter_Gleis_Class import Tkinter_Class

#Gleise instanzieren
Gleis1_Tkinter = Tkinter_Class()
Gleis2_Tkinter = Tkinter_Class()

#Gleistexte definieren
Gleis1_Tkinter.setParameter("Gleis 1",245,700,540,540)
Gleis2_Tkinter.setParameter("Gleis 2",245,700,575,575)

# Ein Fenster erstellen
window = tk.Tk()
# Den Fenstertitle erstellen
window.title("Railway")
window.geometry("1000x700")
canvas = tk.Canvas(window, width=1000, height=700)

Gleis1_Tkinter.label(canvas)
Gleis2_Tkinter.label(canvas)


canvas.pack()



# In der Ereignisschleife auf Eingabe des Benutzers warten.
window.mainloop()
