#!/usr/bin/python3
# -*- encoding: utf8 -*-

from re import match

'''
Regular Expressions for MI
'''

PLUS_MINUS = '[+-]'
INT = '\d+'
DECIMAL = '\d*(\d\.?|\.\d*(_\d+)?)'
# DECIMAL: 0, 0., .0, 0.0, ._0, .0_0, 0._0, 0.0_0
IJ = '[ij]'
COMPLEX = ( # /^[+-]?\d*(\d|\.\d+)([ij]?|[+-]\d*(\d|\.\d+)[ij])?$/
    DECIMAL + '(' + 
    IJ + '?|' + 
    PLUS_MINUS + 
    DECIMAL + 
    IJ + ')?'
)

def half(regex, ifLeft, unsigned = False):
    '''
    When ifLeft == True:
        setting unsigned to True means add no PLUS_MINUS before the regex.
    Otherwise the argument unsigned does nothing.
    '''
    return (
        (
            '^' +
            ('' if unsigned else (PLUS_MINUS + '*')) +
            regex
        ) if ifLeft else
        (regex + '$')
    )
def full(regex, unsigned = False):
    return half(half(regex, True, unsigned), False) # Equiv to left & right