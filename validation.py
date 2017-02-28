#!/usr/bin/python3
# -*- encoding: utf8 -*-

from globalFunc import *

from re import match
import mathRegex as mr

from collections import Iterable

# Debugging Tools
import pdb
t = pdb.set_trace
t = lambda: None

# public section

def typeCheck(arg, tpe):
    'Checks the argument\'s type and raise Error when wrong'
    if not isinstance(arg, tpe): raise TypeError(
        'This function is meant to supplement a method for class ' + tpe.__name__
    )

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
    expression = '^$|' + mr.full(mr.INT)
    if str != type(arg): raise TypeError
    if not match(expression, arg): raise ValueError

# private section

def _isZero(arg):
    'Checks if a number is 0. NOTE: "" is also determined as 0.'
    tpe = type(arg)
    if tpe == str:
        return not [i for i in arg if i != '0']
    else: return arg == 0

def _isInt(arg):
    builtins = [
        int,
        float,
        str,
    ]
    tpe = type(arg)
    expression = mr.full(mr.INT)
    if tpe is int: return True
    if tpe is float: return (0 == arg % 1)
    if tpe is str: return bool(match(expression, arg))
    if not hasattr(arg, '__int__'): return False
    try: return int == type(arg.__int__())
    except: return False
    
