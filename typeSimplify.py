#!/usr/bin/python3
# -*- encoding: utf8 -*-

# Simplification Process:
#
# First: Simplify from complex to real (decimal? frac?)
#
# Second: Simplify from decimal to frac (the other way?) (assuming one is more useful than another)
#
# Third: Simplify from real to integer

from mi import integer, decimal, frac, comp

def typeSimplify(arg):
    'Simplification of Type'
    if not _operatable(arg): raise TypeError
    tpe = type(arg)
    if integer == tpe: return arg
    if tpe in (frac, decimal): return arg if 0 != arg % 1 else typeSimplify(integer(arg))
    if comp == tpe: return arg if 0 != arg.output()[1] else typeSimplify(arg.output()[0])
    
def _operatable(arg):
    ''
    return type(arg) in (integer, decimal, frac, comp)

