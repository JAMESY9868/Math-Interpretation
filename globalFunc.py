#!/usr/bin/python3
# -*- encoding: utf8 -*-
'''
Defines the global functions used in MI system
'''

from fraction import frac
from integer import integer

def sign(arg):
    'Gets the sign of the expression FLAG: NON-EXPR-COMPATIBLE'
    if '__sign__' not in dir(arg): raise TypeError
    arg.__sign__()