#!/usr/bin/python3
# -*- encoding: utf8 -*-

# Does not do anything right now
# pending argument: all

from sys import argv

from globalFunc import *

from integer import *
from fraction import *
from decimal import *
import dec2frac
import cli

def test():
    funcs = [
        testInt,
        testFrac,
    ]
    return [(print(func.__name__), func()) for func in funcs]

def testInt():
    _comboTest(i1, i2)

def testFrac():
    _comboTest(f1, f2)

def _arithmeticTest(first, second):
    'Use all six arithmetic operations to test'
    print('%s + %s = %s' % (first, second, first + second))
    print('%s - %s = %s' % (first, second, first - second))
    print('%s * %s = %s' % (first, second, first * second))
    print('%s / %s = %s' % (first, second, first / second))
    print('%s // %s = %s' % (first, second, first // second))
    print('%s %% %s = %s' % (first, second, first % second))

def _comparisonTest(first, second):
    'Use all six comparison operations to test'
    print('%s == %s: %s' % (first, second, first == second))
    print('%s != %s: %s' % (first, second, first != second))
    print('%s < %s: %s' % (first, second, first < second))
    print('%s <= %s: %s' % (first, second, first <= second))
    print('%s > %s: %s' % (first, second, first > second))
    print('%s >= %s: %s' % (first, second, first >= second))

def _comboTest(first, second):
    'Use both arithmetic and comparion test'
    _arithmeticTest(first, second)
    _comparisonTest(first, second)

# preparation for parsing command line arguments
tester = dict(
    integer = testInt,
    frac = testFrac
)

def mainTest():
    pass

# Test operation starts
if '__main__' == __name__: print(test())
