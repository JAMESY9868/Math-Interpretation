#!/usr/bin/python3
# -*- encoding: utf8 -*-

from re import fullmatch

def _isZero(arg):
    tpe = type(arg)
    if tpe == int:
        return arg == 0
    elif tpe == str:
        return not [i for i in arg if i != '0']


def _isNum(num):
    '''
    Checks if the input is of one of the following types
        int
        str containing ONLY int
    return the decision
    '''
    types = [
        int,
        str,
    ]
    if type(num) not in types: return False
    # check by type
    strMatch = '\d*' # only integers right now
    if str == type(num):
        if not fullmatch(strMatch, num):
            return False
    
    return True

class frac:
    def __init__(self):
        self.nom = ''
        self.denom = ''
    def input(self, nom, denom):
        'Check validity of input set and assign'
        self.inputRaw(nom, denom)
        self.simplify()
        return self
    def inputRaw(self, nom, denom):
        'Check validity of input set and assign'
        # Checking section
        if not (_isNum(nom) or _isNum(denom)): raise TypeError(
                'The arguments provided cannot be interpreted as numbers. Please try other combinations.'
        )
        if _isZero(denom): raise ValueError(
            'The denominator cannot be 0. Please try other values. '
        )
        # Assignment section
        self.nom = str(nom)
        self.denom = str(denom)
        # Return self
        return self
    def simplify(self):
        'Simplify the fraction'
        return self
    def getStr(self):
        'Needs more work here, get the string version of fraction'
        return '(' + self.nom + ')' + '/(' + self.denom + ')'