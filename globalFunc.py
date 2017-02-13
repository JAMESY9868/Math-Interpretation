#!/usr/bin/python3
# -*- encoding: utf8 -*-
import warnings

'''
Defines the global functions used in MI system
'''

def sign(arg):
    'Gets the sign of the expression FLAG: NON-EXPR-COMPATIBLE'
    if '__sign__' not in dir(arg): raise TypeError
    return arg.__sign__()