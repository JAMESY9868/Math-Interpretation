#!/usr/bin/python3
# -*- encoding: utf8 -*-

from globalFunc import *
from validation import *

from integer import *
from gcd import gcd

from re import match
import mathRegex as mr

# Supplement of definition for integer class
integerCheck = lambda arg: typeCheck(arg, integer)
def _intTrueDiv(self, other):
    'A fraction definition of integer trueDiv'
    integerCheck(self)
    if self % other == 0: return self // other
    return frac(self) / frac(other)
def _intFrac(self):
    'fraction conversion for integer'
    integerCheck(self)
    return frac((self, 1))
    
integer.__truediv__ = _intTrueDiv
integer.__frac__ = _intFrac

_DEFAULT_TYPE = integer # the default type of numerator and denominator

class frac:
    def __init__(self, value = None):
        # Default value
        self.input((0, 1))
        # Conversion init
        if value is not None:
            # check if value is of primative types such as int
            tpe = type(value)
            builtins = [
                int,
                float,
                str,
            ]
            # Deal with currently supported types, others raise exception
            if int == tpe: self.input((value, 1))
            elif str == tpe:
                if '/' in value: raise NotImplementedError
                if '.' not in value: self.input(integer(value))
                else: self.input(self.__decimal__().input(value)) # this will raise error without decimal
                return
            elif tpe in builtins: raise NotImplementedError
            # Check if a list-like
            elif ifIterable(value):
                if len(value) < 2: raise ValueError
                self.input(value[:2])
            # then check if __integer__ available
            elif not hasattr(value, '__frac__'): raise NotImplementedError
            else: self.copy(value.__frac__())
            return
    def __frac__(self):
        'Conversion support frac -> frac'
        return self
    def __decimal__(self):
        'support for decimal'
        raise NotImplementedError('Needs to import decimal module')
    def __comp__(self):
        'support for comp'
        raise NotImplementedError('Needs to import comp module')
    
    def output(self):
        'Return a tuple consisting of both the numerator and the denominator'
        return self.numer, self.denom 
    def input(self, value): # numer, denom
        'Check validity of input set and assign'
        if not ifIterable(value): raise TypeError
        if len(value) < 2: raise ValueError
        self.inputRaw(value)
        self.simplify()
        return self
    _inputable = ()
    def inputRaw(self, value): # numer, denom
        'Check validity of input set and assign'
        # Checking section
        if not ifIterable(value): raise TypeError
        if len(value) < 2: raise ValueError
        value = value[:2]
        if {_operatable(e) for e in value} != {True}: return NotImplemented
        zeroCheck(
            value[1],
            'The denominator cannot be 0. Please try other values. '
        )
        # Assignment section
        if True in [isType(e, self._inputable) for e in value]: return frac(value[0]) / frac(value[1])
        self.numer, self.denom = [integer(i) for i in value]
        # Return self
        return self
    
    def simplify(self):
        'Simplify the fraction'
        if 0 == self.output()[0]: return self.inputRaw((0, 1))
        sgn_ = sign(self.output()[0]) * sign(self.output()[1])
        gcd_ = gcd(self.output()[0], self.output()[1])
        return self.inputRaw((sgn_ * abs(self.output()[0]) / gcd_, abs(self.output()[1]) / gcd_))
    
    def copy(self, other):
        'Copy function'
        # strict fraction type
        if not (sameType(frac, self, other)): raise TypeError
        return self.input(other.output())
    
    def inv(self):
        'Inverse the fraction FLAG: LIMIT'
        zeroCheck(self, 'Cannot invert 0.')
        return frac(self.output()[::-1])
    
    def __sign__(self):
        'add support for global sign()'
        return sign(integer(self.output()[0]) * self.output()[1])
    
    def __str__(self):
        'built-in str() support for frac'
        # TODO: remove parentheses in unnecessary cases
        return '%s/%s' % self.output()
    def __repr__(self):
        'built-in repr() support for frac'
        return str(self)
    
    def __abs__(self):
        'built-in abs() support for frac'
        return -self if self.sign() < 0 else self
    def __pos__(self):
        'built-in +A support for frac'
        return self
    def __neg__(self):
        'built-in -A support for frac'
        return frac((-integer(self.output()[0]), self.output()[1]))
    
    def __add__(self, other):
        'built-in A+B support for frac'
        if not _operatable(other): return NotImplemented
        a, b, c, d = [
            integer(e) for e in self.output() + frac(other).output()
        ]
        # a/b + c/d = (ad+bc)/(bd)
        return frac((a * d + b * c, b * d))
    def __radd__(self, other):
        'built-in A+B alternative support for frac'
        return self + other
        
    def __sub__(self, other):
        'built-in A-B support for frac'
        if not _operatable(other): return NotImplemented
        # Return result
        return self + -other
    def __rsub__(self, other):
        'built-in A-B alternative support for frac'
        return -self + other
    
    def __mul__(self, other):
        'built-in A*B support for frac'
        if not _operatable(other): return NotImplemented
        a, b, c, d = self.output() + frac(other).output()
        # a/b * c/d = (ac)/(bd)
        return frac((a * c, b * d))
    def __rmul__(self, other):
        'built-in A*B alternative support for frac'
        return self * other
    
    def __floordiv__(self, other):
        'built-in A//B support for frac, return integer FLAG: EXPR'
        if not _operatable(other): return NotImplemented
        trueDiv = self / other
        if trueDiv < 0: return -(-trueDiv) // 1 - 1
        elif trueDiv == 0: return integer(0)
        return integer(trueDiv.output()[0]) // trueDiv.output()[1]
    def __rfloordiv__(self, other):
        'built-in A//B alternative support for frac'
        return frac(other) // self
        
    def __truediv__(self, other):
        'built-in A/B support for frac FLAG: LIMIT'
        if not _operatable(other): return NotImplemented
        zeroCheck(other, 'Cannot divide by 0')
        return self * frac(other).inv()
    def __rtruediv__(self, other):
        'built-in A/B alternative support for frac'
        return frac(other) / self
    
    def __mod__(self, other):
        'built-in A%B support for frac FLAG: NO-LIMIT'
        if not _operatable(other): return NotImplemented
        return self - other * (self // other)
    def __rmod__(self, other):
        'built-in A%B alternative support for frac'
        return frac(other) % self
    
    def __divmod__(self, other):
        'built-in divmod support for frac'
        return self // other, self % other
    def __rdivmod__(self, other):
        'built-in divmod alternative support for frac'  
        return divmod(frac(other), self)
    ## Conparison Operators
    def __eq__(self, other):
        'built-in A==B support for frac'
        if not _operatable(other): return NotImplemented
        selfSim = self.simplify()
        otherSim = frac(other).simplify()
        return self.simplify().output() == frac(other).output()
    def __ne__(self, other):
        'built-in A!=B support for frac'
        return not (self == other)
    
    def __gt__(self, other):
        'built-in A>B support for frac FLAG: EXPR'
        if not _operatable(other): return NotImplemented
        if type(other) != frac: return self > frac(other)
        ss, so = [sign(e) for e in (self, other)]
        if ss != so: return ss > so # if different sign, compare directly
        if ss < 0: return -self < -other # if ss < 0, reverse sign and compare
        a, b, c, d = [
            integer(e) for e in self.output() + other.output()
        ]
        return abs(a * d) > abs(b * c)
    def __ge__(self, other):
        'built-in A>=B support for frac FLAG: EXPR'
        if type(other) != frac: return self >= frac(other)
        return not self < other # load __lt__
    
    def __lt__(self, other):
        'built-in A<B support for frac FLAG: EXPR'
        if type(other) != frac: return self < frac(other)
        return NotImplemented # force to load __gt__
    def __le__(self, other):
        'built-in A<=B support for frac FLAG: EXPR'
        if type(other) != frac: return self <= frac(other)
        return NotImplemented # force to load __ge__
        
frac._inputable += (frac,)

def _operatable(arg):
    'take the argument itself'
    tpes = (
        # Builtin types
        int,
        float,
        str,
        # MI types
        integer,
        frac,
    )
    return type(arg) in tpes

# TEST AREA
f1 = frac((1, 8))
f2 = frac((3, 4))
