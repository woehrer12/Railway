import tkinter as tk
import functions

gleistext = "1234"
startx = 0
stopx = 0
starty = 0
stopy = 0
idi = 0
gleisbelegt = True

class Tkinter_Class:
    def label(self,window):
        #Text
        x = (self.startx + self.stopx)/2
        y = ((self.starty + self.stopy)/2)-30
        tk.Label(window, text = self.gleistext).place(x = x, y = y)
        #Linie
        window.create_line( self.startx, 
                            self.starty, 
                            self.stopx, 
                            self.stopy, 
                            width=3,
                            arrow=tk.LAST)

        ##Ampel
        self.frameAmpel = tk.Frame(window, background='darkgray')
        self.frameAmpel.place(x=self.stopx -20, y=self.stopy -25, width=35, height=20)
        # Label Rot-Licht
        self.labelRot = tk.Label(self.frameAmpel, background='red')
        self.labelRot.place(x=5, y=5, width=10, height=10)
        # Grün-Licht
        self.labelGruen = tk.Label(self.frameAmpel, background='gray')
        self.labelGruen.place(x=20, y=5, width=10, height=10)

        #Button
        tk.Button(window, text="Hp0", command=self.HP0, width=1, height=1).place(x=x-60,y=y)
        tk.Button(window, text="Hp1", command=self.HP1, width=1, height=1).place(x=x+60,y=y)


    def setParameter(self,text,startx,stopx,starty,stopy,idi):
        self.gleistext = text
        self.startx = startx
        self.stopx = stopx
        self.starty = starty
        self.stopy = stopy
        self.idi = idi


    def HP0(self):
        self.labelRot.config(background='red')
        self.labelGruen.config(background='grey')
        functions.checkidHP0(self.idi)

    def HP1(self):
        self.labelRot.config(background='grey')
        self.labelGruen.config(background='green')
        functions.checkidHP1(self.idi)    

    def isbelegt(self):
        return self.gleisbelegt

    def setbelegt(self):
        self.gleibelegt = True

    def setfrei(self):
        self.gleisbelegt = False

    