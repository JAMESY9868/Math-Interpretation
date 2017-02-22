#!/usr/bin/python3
# -*- encoding: utf8 -*-

from globalFunc import *
from validation import *
from validation import _isZero as isZero

from integer import *
from fraction import *

from re import match
import mathRegex as mr

# Supplement of definition for frac class
fracCheck = lambda arg: typeCheck(arg, frac)
def _fracDec(self):
    'decimal conversion for frac'
    # Type Check
    fracCheck(self)
    # Conversion
    outStr = [str(each) for each in self.output()]
    if sign(self) < 0: return -_fracDec(-self)
    integ = self // 1
    if integ > 0: return decimal((integ,)) + decimal(self - integ)
    if '0' == outStr[0]: return decimal(0)
    expression = mr.full('10*')
    # Cannot use decimal arithmetic operations because that would be cross-reference
    if match(expression, outStr[1]):
        if len(outStr[0]) < len(outStr[1]): return decimal((
            0, '0' * (len(outStr[1]) - len(outStr[0]) - 1) + outStr[0]
        ))
    raise NotImplementedError
def _intDec(self):
    'decimal conversion for integer'
    # Type Check
    integerCheck(self)
    # Conversion
    return decimal((self,))
    
frac.__decimal__ = _fracDec

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
                expression = mr.full(mr.DECIMAL)
                if not match(expression, value): raise ValueError
                intDec = value.split('.')
                if len(intDec) < 2: self.input((intDec[0],)); return
                finInf = intDec[1].split('_')
                self.input(intDec) if len(finInf) < 2 else self.input([intDec[0]] + finInf)
            elif tpe in builtins: raise NotImplementedError
            elif ifIterable(value):
                if len(value) > 2: numLiteralCheck(str(value[2]))
                if len(value) > 1: numLiteralCheck(str(value[1]))
                numLiteralCheck(str(value[0]))
                self.input(value)
            elif not hasattr(value, '__decimal__'): raise TypeError
            else: self.copy(value.__decimal__())
            return
    def __decimal__(self):
        'decimal conversion support'
        return self
    def __frac__(self):
        'frac conversion support'
        output = self.output()
        if sign(output[0]) < 0: return -decimal((-output[0], *output[1:])).__frac__()
        if not isZero(output[2]) and sum([not isZero(e) for e in output[:2]]):
            # if [0] and [1] not both empty, and [2] not empty -- use separation
            return (
                decimal(output[:2]).__frac__() +
                decimal(('',) * 2 + output[2:]).__frac__() / integer('1' + '0' * len(output[1]))
            )
        if not isZero(output[2]):
            # if [2] not empty (implying [0] and [1] both empty): case of ._34
            #raise NotImplementedError # not yet figured out
            return frac((
                output[2], '9' * len(output[2]) + '0' * len(output[1])
            ))
        if isZero(output[0]):
            # if [0] empty (implying [1] not empty): case of .2, -.345
            return frac((output[1], '1' + '0' * len(output[1])))
        if isZero(output[1]):
            # if [1] empty (implying [0] not empty): case of 1.0, -2.000, 3., -4
            return frac(output[0]) # return the integer as a fraction
        # implying [0] [1] both with value -- use separation: case of 1.234, -4.53
        return decimal(output[:1]).__frac__() + decimal((0,) + output[1:2]).__frac__()
        
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
            checkFunc = numLiteralCheck
            [checkFunc(str(arg)) for arg in value]
            l = len(value)
            if l > 2: self.infDec = value[2]
            if l > 1: self.finDec = value[1]
            self.integ = integer(value[0])
        else: self.input(decimal(value).output())
    def copy(self, other):
        'Copy function'
        # Strict decimal type
        if not (type(self) == decimal == type(other)): raise TypeError
        return self.input(other.output())
    def __repr__(self):
        'built-in repr support for decimal'
        return str(self)
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
    # Arithmetic Operators -- common idea: change to fraction
    def __pos__(self):
        'built-in support of +A'
        return self
    def __neg__(self):
        'built-in support of -A'
        return decimal((-self.output()[0], *self.output()[1:]))
    def __add__(self, other):
        'built-in support of A+B'
        return frac(self) + frac(other)
    def __radd__(self, other):
        'built-in alternative support of A+B with B type decimal'
        return self + decimal(other)
    def __sub__(self, other):
        'built-in support of A-B'
        return self + -other
    def __rsub__(self, other):
        'built-in alternative support of A-B'
        return self - decimal(other)
    def __mul__(self, other):
        'built-in support of A*B'
        return decimal(frac(self) * frac(other))
    def __floordiv__(self, other):
        'built-in support of A//B'
        return decimal(frac(self) // frac(other))
    def __truediv__(self, other):
        'built-in support of A/B'
        return decimal(frac(self) / frac(other))
    def __mod__(self, other):
        'built-in support of A%B'
        return decimal(frac(self) % frac(other))
    # Conparison Operators -- common idea: change to fraction
    def __eq__(self, other):
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

# TEST AREA
d1 = decimal('1.2_3')
d2 = decimal('3.3')
mode = 5 # subtraction
