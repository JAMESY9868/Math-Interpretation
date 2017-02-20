#!/usr/bin/python3
# -*- encoding: utf8 -*-
from globalFunc import *
from validation import *

from fraction import *

from re import match
import mathRegex as mr

from validation import _isZero as isZero

# Debug tool
import pdb
t = pdb.set_trace

# NOTE: This is a temporary version of decimal.__frac__
# which impies the type of strDec as str, 
# whereas the final decimal.__frac__ will be implied as type decimal.

# KNOWN BUG: -1.234 is seperated into -1.0 and .234

def dec2frac(strDec):
    'input str, return frac, finite decimal'
    # Check if is str, and matches the re
    if type(strDec) is not str: raise TypeError
    expression = mr.full(mr.DECIMAL)
    if not match(expression, strDec): raise ValueError
    # Extract out negative sign
    if '-' == strDec[0]: return -dec2frac(strDec[1:])
    # Seperate to list
    lstDec = strDec.split('.')
    # case of 1.0, -2.000, 3.
    if isZero(lstDec[1]): return frac((lstDec[0], 1))
    # case of 1.234, -4.53
    elif not isZero(lstDec[0]): return (
        dec2frac(lstDec[0] + '.') +
        dec2frac('.' + lstDec[1])
    )
    # case of .2, -.345
    return frac((lstDec[1], '1' + '0' * len(lstDec[1]))) 
    
def decInf2frac(strDec):
    'input str, return frac, repeating infinite decimal'
    pass


dec2frac('-1.2')