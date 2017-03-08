#!/usr/bin/python3
# -*- encoding: utf8 -*-

import validation

'''
Defines the global functions used in MI system
'''

def sign(arg):
    'Gets the sign of the expression FLAG: NON-EXPR-COMPATIBLE'
    if not hasattr(arg, '__sign__'): raise TypeError
    return arg.__sign__()

def signStr(arg, optPlusSign = False):
    'Gets the sign of the expression with + or -, or if optPlusSign is False (by default), empty string.' 
    return '-' if sign(arg) < 0 else '+' if optPlusSign else ''

def size(arg):
    'Gets the size of a vector or a matrix'
    if not hasattr(arg, '__size__'): raise TypeError
    return arg.__size__()

# the following lines simply serve for the ease of typing, and can/should be ignored.
alternative = 0; del alternative
support = 0; del support
