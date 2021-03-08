#!/usr/bin/python
#-*- coding:utf-8 -*-

#from tkinter import *
import tkinter as tk
from tkinter import messagebox, filedialog
from Tkinter_Gleis_Class import Tkinter_Class
import functions

#Gleise instanzieren
Gleis1_Tkinter = Tkinter_Class()
Gleis2_Tkinter = Tkinter_Class()
Gleis3_Tkinter = Tkinter_Class()
Gleis4_Tkinter = Tkinter_Class()
Gleis5_Tkinter = Tkinter_Class()
Gleis6_Tkinter = Tkinter_Class()
Gleis7_Tkinter = Tkinter_Class()
Gleis8_Tkinter = Tkinter_Class()
Gleis9_Tkinter = Tkinter_Class()
Gleis10_Tkinter = Tkinter_Class()

#Gleise definieren
Gleis1_Tkinter.setParameter("Gleis 1",245,700,540,540,1)
Gleis2_Tkinter.setParameter("Gleis 2",245,700,575,575,2)
Gleis3_Tkinter.setParameter("Gleis 3",785,925,540,400,3)
Gleis4_Tkinter.setParameter("Gleis 4",925,850,250,135,4)
Gleis5_Tkinter.setParameter("Gleis 5",755,185,90,90,5)
Gleis6_Tkinter.setParameter("Gleis 6",710,235,110,110,6)
Gleis7_Tkinter.setParameter("Gleis 7",645,300,140,140,7)
Gleis8_Tkinter.setParameter("Gleis 8",645,300,170,170,8)
Gleis9_Tkinter.setParameter("Gleis 9",90,20,130,330,9)
Gleis10_Tkinter.setParameter("Gleis 10",20,160,400,540,10)



# Ein Fenster erstellen
window = tk.Tk()
# Den Fenstertitle erstellen
window.title("Railway")
window.geometry("1000x700")
canvas = tk.Canvas(window, width=1000, height=700)

#Gleise Aufrufen
Gleis1_Tkinter.label(canvas)
Gleis2_Tkinter.label(canvas)
Gleis3_Tkinter.label(canvas)
Gleis4_Tkinter.label(canvas)
Gleis5_Tkinter.label(canvas)
Gleis6_Tkinter.label(canvas)
Gleis7_Tkinter.label(canvas)
Gleis8_Tkinter.label(canvas)
Gleis9_Tkinter.label(canvas)
Gleis10_Tkinter.label(canvas)


canvas.pack()

# In der Ereignisschleife auf Eingabe des Benutzers warten.
window.mainloop()
