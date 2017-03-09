#!/usr/bin/python3
# -*- encoding: utf8 -*-

# Does not do anything right now
# pending argument: all

from sys import argv

from globalFunc import *
from validation import *

from mi import *

import cli

import color

extraArg = {
    'all' : False,
    'oper' : False,
}

_limited = {
    'arithmetic' : (comp, vector),
    'comparison' : (comp, vector),
}

all = (
    (i1, i2),
    (f1, f2),
    (d1, d2),
    (c1, c2),
    (v1, v2),
)

def test():
    if 'quiet' in argv: # quiet mode
        global print; print = lambda *_: None
    if 'all' in argv: 
        extraArg['oper'] = True
    if 'oper' in argv: extraArg['oper'] = True
    funcs = (
        testInt,
        testFrac,
        testDec,
        testComp,
        testVector,
        
        interTest,
    )
    return [(print(), print(color.color('yellow').text(func.__name__)), func()) for func in funcs]

def combo(i, ifRemode = False):
    _comboTest(*[(e if not ifRemode else e.remode(False)) for e in all[i]])

def testInt():
    combo(0) # integer

def testFrac():
    combo(1) # frac

def testDec():
    combo(2) # decimal

def testComp():
    combo(3) # comp
    combo(3, True)

def testVector():
    _comboTest(v1, v2)

def interTest():
    l = len(all)
    for i in range(l):
        for j in range(i, l):
            for n in range(2):
                _comboTest(*((all[i][n], all[j][n])[::[1, -1][n]]))

_beginEnd = lambda colorStr: (
    lambda: print(color.color(colorStr).str()),
    lambda: print(color.color().str()),
)

def _arithmeticTest(first, second):
    'Use all six arithmetic operations to test'
    BEGIN, END = _beginEnd('magenta')
    BEGIN()
    print('(%s) + (%s) = %s' % (first, second, first + second))
    print('(%s) - (%s) = %s' % (first, second, first - second))
    print('(%s) * (%s) = %s' % (first, second, first * second))
    print('(%s) / (%s) = %s' % (first, second, first / second))
    if True in [isType(e, _limited['arithmetic']) for e in (first, second)]: return END()
    #if type(first) in _limited['arithmetic']: return END()
    #if type(second) in _limited['arithmetic']: return END()
    print('(%s) // (%s) = %s' % (first, second, first // second))
    print('(%s) %% (%s) = %s' % (first, second, first % second))
    print('divmod(%s, %s) = %s, %s' % ((first, second) + divmod(first, second)))
    return END()

def _comparisonTest(first, second):
    'Use all six comparison operations to test'
    BEGIN, END = _beginEnd('green')
    BEGIN()
    print('(%s) == (%s): %s' % (first, second, first == second))
    print('(%s) != (%s): %s' % (first, second, first != second))
    if True in [isType(e, _limited['comparison']) for e in (first, second)]: return END()
    print('(%s) < (%s): %s' % (first, second, first < second))
    print('(%s) <= (%s): %s' % (first, second, first <= second))
    print('(%s) > (%s): %s' % (first, second, first > second))
    print('(%s) >= (%s): %s' % (first, second, first >= second))
    return END()

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
if '__main__' == __name__: test()
