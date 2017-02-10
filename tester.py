#!/usr/bin/python3
# -*- encoding: utf8 -*-

# Does not do anything right now
# pending argument: all

from globalFunc import *

from integer import integer
from fraction import frac
import dec2frac

def test():
    funcs = [
        testFrac,
    ]
    return sum([func() for func in funcs])

def testFrac():
    ans = True
    f = frac()
    f.input(1, 2)
    ans ^= '(1)/(2)' == str(f)
    return ans


if '__main__' == __name__: print(test())
