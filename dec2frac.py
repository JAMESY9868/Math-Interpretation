#!/usr/bin/python3
# -*- encoding: utf8 -*-
from fraction import frac
from fraction import _isZero
from re import match

def dec2frac(strDec):
    'input str, return frac'
    # Check if is str, and matches the re
    if type(strDec) is not str: raise TypeError
    expression = '^(?=.{2,})\d*\.\d+$' # matches strict decimals (12.3, not 12. or 12; .3 works as well)
    if not match(expression, strDec): raise ValueError
    # Seperate to list
    lstDec = strDec.split('.')
    # case of 1.0, 2.000
    if not [i for i in lstDec[1] if i != '0']: return frac().input(lstDec[0], 1)
    # case of .2, .345
    pass
    # case of 1.234, 4.53
    pass