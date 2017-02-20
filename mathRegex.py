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

def full(regex):
    return (
        '^' + PLUS_MINUS + '?' + regex + '$'
    )