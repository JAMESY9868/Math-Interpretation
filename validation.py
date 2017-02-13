#!/usr/bin/python3
# -*- encoding: utf8 -*-

from globalFunc import *

from collections import Iterable

# public section

def zeroCheck(num, messege = ''):
    'A fast way of checking if a number is 0'
    if _isZero(num): raise ValueError(messege)
    
def intCheck(num):
    if not _isInt(num): raise TypeError    
    
def ifIterable(arg):
    'Checks if an item is Iterable'
    return isinstance(arg, Iterable)

def numLiteralCheck(arg):
    'Checks if an item is a numerical literal (including empty)'
    expression = '^\d*$'
    if str != type(arg): raise TypeError
    if not match(expression, arg): raise ValueError

# private section

def _isZero(arg):
    'Checks if a number is 0. NOTE: "" is also determined as 0.'
    tpe = type(arg)
    if tpe == str:
        return not [i for i in arg if i != '0']
    else: return arg == 0

def _isInt(num):
    types = [
        int,
        str,
        integer,
    ]
    if type(num) not in types: return False
    expression = '^-?\d+$'
    if str == type(num):
        if not match(expression, num): return False
    return True

