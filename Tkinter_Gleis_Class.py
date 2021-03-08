import tkinter as tk

gleistext = "1234"
startx = 0
stopx = 0
starty = 0
stopy = 0

class Tkinter_Class:
    def label(self,window):
        x = (self.startx + self.stopx)/2
        y = ((self.starty + self.stopy)/2)-30
        tk.Label(window, text = self.gleistext).place(x = x, y = y)
        window.create_line( self.startx, 
                            self.starty, 
                            self.stopx, 
                            self.stopy, 
                            arrow=tk.LAST)

    def arrow(self,canvas):
        print("123")


    def setParameter(self,text,startx,stopx,starty,stopy):
        self.gleistext = text
        self.startx = startx
        self.stopx = stopx
        self.starty = starty
        self.stopy = stopy
