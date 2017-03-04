#!/usr/bin/python3
# -*- encoding: utf8 -*-

# Does not do anything right now
# pending argument: all

from sys import argv

from globalFunc import *

from integer import *
from fraction import *
from decimal import *
from complex import *
import cli

import color

extraArg = {
    'all' : False,
    'oper' : False,
}

_limited = {
    'arithmetic' : (comp,),
    'comparison' : (comp,),
}

def test():
    if 'all' in argv: 
        extraArg['oper'] = True
    if 'oper' in argv: extraArg['oper'] = True
    funcs = (
        testInt,
        testFrac,
        testDec,
        testComp,
    )
    return [(print(func.__name__), func()) for func in funcs]

def testInt():
    _comboTest(i1, i2)

def testFrac():
    _comboTest(f1, f2)

def testDec():
    _comboTest(d1, d2)

def testComp():
    _comboTest(c1, c2)
    _comboTest(c1.remode(False), c2.remode(False))

def _arithmeticTest(first, second):
    'Use all six arithmetic operations to test'
    print('%s + %s = %s' % (first, second, first + second))
    print('%s - %s = %s' % (first, second, first - second))
    print('%s * %s = %s' % (first, second, first * second))
    print('%s / %s = %s' % (first, second, first / second))
    if type(first) in _limited['arithmetic']: return
    if type(second) in _limited['arithmetic']: return
    print('%s // %s = %s' % (first, second, first // second))
    print('%s %% %s = %s' % (first, second, first % second))
    print('divmod(%s, %s) = %s, %s' % ((first, second) + divmod(first, second)))

def _comparisonTest(first, second):
    'Use all six comparison operations to test'
    print('%s == %s: %s' % (first, second, first == second))
    print('%s != %s: %s' % (first, second, first != second))
    if type(first) in _limited['comparison']: return
    if type(second) in _limited['comparison']: return
    print('%s < %s: %s' % (first, second, first < second))
    print('%s <= %s: %s' % (first, second, first <= second))
    print('%s > %s: %s' % (first, second, first > second))
    print('%s >= %s: %s' % (first, second, first >= second))

def _operatorExistTest(arg):
    'Checks if all necessary operator wrappers are present'
    opers = (
        '__pos__', '__neg__',
        '__add__', '__radd__',
        '__sub__', '__rsub__',
        '__mul__', '__rmul__',
        '__truediv__', '__rtruediv__',
        '__floordiv__', '__rfloordiv__',
        '__mod__', '__rmod__',
        '__divmod__', '__rdivmod__',
        '__eq__', '__ne__',
        '__gt__', '__ge__',
        '__lt__', '__le__',
    )
    missingArg = [
        oper for oper in opers
        if not hasattr(arg, oper)
    ]
    
    print(color.color('red').text('Missing operators for type %s: %s' %
        (type(arg).__name__, missingArg)))
    if extraArg['oper']: 
        if len(missingArg) != 0: raise AttributeError

def _comboTest(first, second):
    'Use all available tests for a certain class'
    _operatorExistTest(first)
    _arithmeticTest(first, second)
    _comparisonTest(first, second)
    print()

# preparation for parsing command line arguments
tester = {
    'integer' : testInt,
    'frac' : testFrac,
    'decimal' : testDec,
    'comp' : testComp,
}

def mainTest():
    pass

# Test operation starts
if '__main__' == __name__: print(test())
