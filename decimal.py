#!/usr/bin/python3
# -*- encoding: utf8 -*-

from globalFunc import *
from validation import *

from integer import *
from fraction import *
from re import match

_DEFAULT_TYPE = (integer, str, str)

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
                self.input(intDec) if len(finInf) < 2 else self.input([intDec[0]] + finInf)
            elif tpe in builtins: raise NotImplementedError
            elif ifIterable(value):
                intCheck(value[0])
                if len(value) > 2: numLiteralCheck(value[2])
                if len(value) > 1: numLiteralCheck(value[1])
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
            checkFunc = [intCheck, numLiteralCheck, numLiteralCheck] # both functions raise exceptions when req not met
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
    def sign(self):
        'sign of decimal'
        pass
    def __sign__(self):
        'globalFunc sign function support'
        return decimal(
            1 if self > 0 else
            -1 if self < 0 else
            0
        )
    # Arithmetic Operators
    # Conparison Operators -- common idea: change to fraction
    def __eq__(self, ohter):
        'built-in support of A==B'
        return frac(self) == frac(other)
    def __ne__(self, other):
        'built-in support of A!=B'
        return not (self == other)
    def __gt__(self, other):
        'built-in support of A>B'
        return frac(self) > frac(other)
    def __ge__(self, other):
        'built-in support of A>=B'
        return not (self < other)
    def __lt__(self, other):
        'built-in support of A<B'
        return NotImplemented # call __gt__
    def __le__(self, other):
        'built-in support of A<=B'
        return NotImplemented # call __ge__
