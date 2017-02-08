#!/usr/bin/python3
#! -*- encoding: utf8 -*-
from fraction import frac
from re import match, fullmatch

def isZero(arg):
    tpe = type(arg)
    if tpe == int:
        return arg == 0
    elif tpe == str:
        return not [i for i in arg if i != '0']

def dec2frac(strDec):
    'input str, return frac'
    # Check if is str, and matches the re
    if type(strDec) is not str: raise TypeError
    expression = '^(?={2,}\d*\.\d+$'
    if not fullmatch(expression, strDec): raise ValueError
    # Seperate to list
    lstDec = strDec.split('.')
    if [i for i in lstDec[1] if i != '0']: return frac.input(lstDec[0], 1)
    