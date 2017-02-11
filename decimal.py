#!/usr/bin/python3
# -*- encoding: utf8 -*-

from fraction import frac
from integer import integer, _intCheck
from collections import Iterable
from re import match

class decimal:
    def __init__(self, value = None):
        '''
        input for decimal [does not support irregular infinite decimal]:
        possible types:
        1. str matching /^-?\d*(\d|\.\d*(_\d+)?)$/
            /^\d+$/ integer-like, '1'
            /^\d*\.\d+$/ finite decimal '1.' or '1.2'
            /^\d*\.\d*_\d+$ repeating infinite decimal '1.2_3', '1._3', where '_' represents the starting point of the repeating part
        2. decimal value
        3. frac value
        4. integer value
        5. iterable object with type (A, [str, [str]]) where A can be converted to integer
        6. int, float
        '''
        # Fields with default values
        self.integ = integer(0) # integer part, default type integer
        self.finDec = '' # finite decimal part, default type str
        self.infDec = '' # infinite decimal part, default type str
        # Conversion init
        if value is not None:
            builtins = [
                # decimal,
                # frac,
                # integer,
                str,
                int,
                float,
            ]
            tpe = type(value)
            if tpe == int: self.input((value,))
            elif tpe == str: 
                expression = '^-?\d*(\d|\.\d*(_\d+)?)$'
                if not match(expression, value): raise ValueError
                intDec = value.split('.')
                if len(intDec) < 2: self.input((intDec[0]),); return
                finInf = intDec[1].split('_')
                self.input(intDec) if len(finInf) < 2 else self.input((intDec[0], *finInf))
            elif tpe in builtins: raise NotImplementedError
            elif ifIterable(value):
                _intCheck(value[0])
                if len(value) > 2: _strNumCheck(value[2])
                if len(value) > 1: _strNumCheck(value[1])
            elif '__decimal__' not in dir(value): raise TypeError
            else: self.input(value.__decimal__().value)
            return
    def __decimal__(self):
        'decimal conversion support'
        return self
    def __frac__(self):
        'frac conversion support'
        pass
    def __integer__(self):
        'integer conversion support'
        return integer(self.integ)
    def output(self):
        '''
        output a tuple consisting of three parts:
        1. integer part, type integer
        2. non-repeating part, type str
        3. repeating part, type str
        '''
        return (self.integ, self.finDec, self.infDec)
    def input(self, value):
        '''
        input for decimal [does not support irregular infinite decimal]:
        possible types:
        1. str matching /^-?\d*(\d|\.\d*(_\d+)?)$/
            /^\d+$/ integer-like, '1'
            /^\d*\.\d+$/ finite decimal '1.' or '1.2'
            /^\d*\.\d*_\d+$ repeating infinite decimal '1.2_3', '1._3'
        2. decimal value
        3. frac value
        4. integer value
        5. iterable object with type (A, [str, [str]]) where A can be converted to integer
        6. int, float
        '''
        if ifIterable(value):
            checkFunc = [_intCheck, _strNumCheck, _strNumCheck] # both functions raise exceptions when req not met
            [func(arg) for arg, func in zip(value, checkFunc)]
            l = len(value)
            if l > 2: self.infDec = value[2]
            if l > 1: self.finDec = value[1]
            self.integ = value[0]
        else: self.input(_THIS_CLASS(value).output())
    def str(self):
        'string version'
        return str(self)
    def __str__(self):
        'built-in str support for decimal'
        return (
            str(self.integ) + # first part
            (
                ('.' + self.finDec) # second part, if with decimal
                 if self.finDec else
                '.' if self.infDec else ''
            ) + 
            (
                ('_' + self.infDec) # third part, if with repetition
                if self.infDec else ''
            )
        )
def ifIterable(arg):
    'Checks if an item is Iterable'
    return isinstance(arg, Iterable)

def _strNumCheck(arg):
    'Checks if an item is a string representation of a number'
    expression = '^\d*$'
    if str != type(arg): raise TypeError
    if not match(expression, arg): raise ValueError

_DEFAULT_TYPE = (integer, str, str)
_THIS_CLASS = decimal
