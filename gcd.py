#!/usr/bin/python3
# -*- encoding: utf8 -*-

from integer import integer
from validation import zeroCheck # Exception if 0

def gcd(first, second):
    'Checks if convertible to integer'
    return _gcd(abs(integer(first)), abs(integer(second)))
def _gcd(firstInt, secondInt):
    'Internal Process, assumed non-neg integer type'
    [zeroCheck(n) for n in [firstInt, secondInt]]
    if firstInt > secondInt: return _gcd(secondInt, firstInt)
    # Assumed firstInt < secondInt
    if secondInt % firstInt == 0: return firstInt
    return _gcd(secondInt % firstInt, firstInt)
    
pass