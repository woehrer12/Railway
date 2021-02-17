

class Gleis:
    istbelegt = False
    sollbelegt = False
    nächstesGleisbelegt = True
    H0 = False

    def loop(self):
        if Gleis.nächstesGleisbelegt == True:
            Gleis.H0 = True

    def getbelegt(self):
        return Gleis.istbelegt or Gleis.sollbelegt

    def getnächtesbelegt(self):
        return Gleis.nächstesGleisbelegt

    def getH0(self):
        return Gleis.H0
