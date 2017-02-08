#!/usr/bin/python3

def _numValidity(num):
    pass

class frac:
    def __init__(self):
        self.nom = ''
        self.denom = ''
    def input(self, nom, denom):
        'Check validity of input set and assign'
        pass
    def inputRaw(self, nom, denom):
        'Check validity of input set and assign'
        # Checking section
        if _numValidity(nom) or _numValidity(denom):
            pass
        # Assignment section
        self.nom = str(nom)
        self.denom = str(denom)
    def simplify(self):
        'Simplify the fraction'
        pass