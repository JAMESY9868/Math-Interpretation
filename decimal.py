#!/usr/bin/python3
# -*- encoding: utf8 -*-

from prototypes.rational import rational

from globalFunc import *
from validation import *
from validation import _isZero as isZero

from integer import *
from fraction import *

from re import match
import mathRegex as mr

from primePow import *
from gcd import lcm

# Supplement of definition for frac class
fracCheck = lambda arg: typeCheck(arg, frac)
def _fracDec(self):
    'decimal conversion for frac'
    # Type Check
    fracCheck(self)
    if sign(self) < 0: return -_fracDec(-self) # turn all negatives into positives
    integ = self // 1 # separate integer part and pure decimal part
    self %= 1
    # Conversion
    outStr = [str(each) for each in self.output()]
    if '0' == outStr[0]: return decimal(integ)
    #raise NotImplementedError
    alpha, beta = [primePow(outStr[1], i) for i in (2, 5)] # power of 2 | 5 in the denominator
    nonRepeatNum = max(alpha, beta) # The non-repeating part of the decimal
    n_0 = integer(outStr[1]) / integer(2) ** alpha / integer(5) ** beta
    ind = 1 # it seems that currently integer.__rpow__ is not working so fall back to int
    while n_0 > 1:
        if 1 == (10 ** ind) % n_0: break
        ind += 1
    repeatNum = ind
    newNumer = integer(outStr[0]) * 10 ** (nonRepeatNum + repeatNum)
    newResult = newNumer // outStr[1]
    repeating, nonRepeat = divmod(newResult, 10 ** repeatNum)[::-1]
    emptyZero = lambda num: '' if (0 == num) else str(num)
    fillZero = lambda num, count: (
        (('0' * integer(count - len(emptyZero(num))).output()) if (-1 < count - len(emptyZero(num))) else '') + 
        emptyZero(num)
    )
    return decimal((integ, fillZero(nonRepeat, nonRepeatNum), fillZero(repeating, repeatNum)))
    
def _intDec(self):
    'decimal conversion for integer'
    # Type Check
    integerCheck(self)
    # Conversion
    return decimal((self,))
    
frac.__decimal__ = _fracDec
integer.__decimal__ = _intDec

_DEFAULT_TYPE = (integer, str, str)

class decimal(rational):
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
    def __init__(self, value = None, **extra):
        # Fields with default values
        self.input((0, '', '')) # Default type: integer, str, str
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
                integ = integer(value[0])
                numLiteralCheck(str(abs(integ)))
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
        if sign(output[0]) < 0: return -decimal((-output[0],) + output[1:]).__frac__()
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
        return integer(self.output()[0])
    def __comp__(self):
        'support for comp'
        raise NotImplementedError('Needs to import comp module')
    
    def output(self):
        '''
        output a tuple consisting of three parts:
        1. integer part, type integer
        2. non-repeating part, type str
        3. repeating part, type str
        '''
        return self.integ, self.finDec, self.infDec
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
            zeroMatch = lambda x: match(mr.full('0+'), str(x))
            if l > 2: self.infDec = str(value[2]) if not zeroMatch(value[2]) else ''
            if l > 1: self.finDec = str(value[1]) if not (self.infDec == '' and zeroMatch(value[1])) else ''
            self.integ = integer(value[0])
        else: self.input(decimal(value).output())
        return self
    def copy(self, other):
        'Copy function'
        # Strict decimal type
        if not (type(self) == decimal == type(other)): raise TypeError
        return self.input(other.output())
    
    def simplify(self):
        'Simplify decimal'
        return self.input(decimal(frac(self)))
    
    def __repr__(self):
        'built-in repr support for decimal'
        return str(self)
    def __str__(self):
        'built-in str support for decimal'
        return (
            str(self.output()[0]) + # first part
            (
                ('.' + self.output()[1]) # second part, if with decimal
                 if self.output()[1] else
                '.' if self.output()[2] else ''
            ) + 
            (
                ('_' + self.output()[2]) # third part, if with repetition
                if self.output()[2] else ''
            )
        )
    def __sign__(self):
        'globalFunc sign function support'
        return integer(
            1 if self > 0 else
            -1 if self < 0 else
            0
        )
    # Arithmetic Operators -- common idea: change to fraction
    def __abs__(self):
        'built-in abs support for decimal'
        return self if self.output()[0] > 0 else -self
    def __pos__(self):
        'built-in +A support for decimal'
        return self
    def __neg__(self):
        'built-in -A support for decimal'
        return decimal((-self.output()[0],) + self.output()[1:])
    
    def __add__(self, other):
        'built-in A+B support for decimal'
        if not _operatable(other): return NotImplemented
        return decimal(frac(self) + frac(other))
    def __radd__(self, other):
        'built-in A+B alternative support for decimal'
        return self + decimal(other)
    
    def __sub__(self, other):
        'built-in A-B support for decimal'
        return self + -other
    def __rsub__(self, other):
        'built-in A-B alternative support for decimal'
        return self - decimal(other)
    
    def __mul__(self, other):
        'built-in A*B support for decimal'
        if not _operatable(other): return NotImplemented
        return decimal(frac(self) * frac(other))
    def __rmul__(self, other):
        'built-in A*B alternative support for decimal'
        return self * other
    
    def __floordiv__(self, other):
        'built-in A//B support for decimal'
        if not _operatable(other): return NotImplemented
        return decimal(frac(self) // frac(other))
    def __rfloordiv__(self, other):
        'built-in A//B alternative support for decimal'
        return decimal(other) // self
    
    def __truediv__(self, other):
        'built-in A/B support for decimal'
        if not _operatable(other): return NotImplemented
        return decimal(frac(self) / frac(other))
    def __rtruediv__(self, other):
        'built-in A/B alternative support for decimal'
        return decimal(other) / self
    
    def __mod__(self, other):
        'built-in A%B suppoort for decimal'
        if not _operatable(other): return NotImplemented
        return decimal(frac(self) % frac(other))
    def __rmod__(self, other):
        'built-in A%B alternative support for decimal'
        return decimal(other) % self
    
    def __divmod__(self, other):
        'built-in divmod support for decimal'
        return self // other, self % other
    def __rdivmod__(self, other):
        'built-in divmod alternative support for decimal'
        return divmod(decimal(other), self)
    # Conparison Operators -- common idea: change to fraction
    def __eq__(self, other):
        'built-in support of A==B'
        if not _operatable(other): return NotImplemented
        return frac(self) == frac(other)
    def __ne__(self, other):
        'built-in support of A!=B'
        return not (self == other)
    def __gt__(self, other):
        'built-in support of A>B'
        if not _operatable(other): return NotImplemented
        return frac(self) > frac(other)
    def __ge__(self, other):
        'built-in support of A>=B'
        return not (self < other)
    def __lt__(self, other):
        'built-in support of A<B'
        if not _operatable(other) or decimal == type(other): return NotImplemented
        return self < decimal(other)
    def __le__(self, other):
        'built-in support of A<=B'
        if not _operatable(other) or decimal == type(other): return NotImplemented
        return self <= decimal(other)
    # OPERATABILITY
    @staticmethod
    def __operatable(arg):
        'Checks if the argument is operatable'
        tpes = (
            int,
            float,
            str,
            integer,
            frac,
            decimal,
        )
        return type(arg) in tpes

_operatable = decimal._decimal__operatable

# TEST AREA
d1 = decimal('1.2_3')
d2 = decimal('._3')
