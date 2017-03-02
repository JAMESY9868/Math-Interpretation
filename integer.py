#!/usr/bin/python3
# -*- encoding: utf8 -*-

#
# Current idea is to use an int to represent the number
# with customized methods connecting to other objects
#

from globalFunc import *
from validation import *

from re import match

_DEFAULT_TYPE = int # the default type of value held inside the class

class integer:
    def __init__(self, value = None):
        # Default init
        self.input(0)
        # Conversion init
        if value is not None:
            tpe = type(value)
            # check if value is of primative types such as int, str
            builtins = [
                int,
                float,
                str,
            ]
            # Deal with currently supported types, others raise exception
            if int == tpe: self.input(value)
            elif str == tpe:
                if '' == value: self.input(0)
                else: self.input(int(value))
            elif tpe in builtins: raise NotImplementedError
            # then check if __integer__ available
            elif not hasattr(value, '__integer__'): raise TypeError
            else: self.copy(value.__integer__())
            return
    def __integer__(self):
        'support for integer constructor'
        return self
    def output(self):
        'The output function for integer'
        return self.value
    def input(self, value):
        'the input function for integer'
        if _DEFAULT_TYPE != type(value): return self.copy(integer(other))
        self.value = value
        return self
    def copy(self, other):
        'copy function'
        # strict same type
        if not sameType(integer, self, other): raise TypeError
        return self.input(other.output())
    
    def __frac__(self):
        'support for frac'
        raise NotImplementedError(
            'Needs to import fraction module'
        )
    def __decimal__(self):
        'support for decimal'
        raise NotImplementedError(
            'Needs to import decimal module'
        )
    def __comp__(self):
        'support for comp'
        raise NotImplementedError(
            'Needs to import complex module'
        )
    
    def __str__(self):
        'built-in str support for integer'
        return str(self.output())
    def __repr__(self):
        'built-in repr support for integer'
        return str(self)
    
    def __sign__(self):
        'add support for global sign()'
        return 0 if 0 == self else (self // abs(self))
    
    def __abs__(self):
        'built-in abs support for integer'
        return integer(abs(self.output()))
    def __pos__(self):
        'built-in +A support for integer'
        return self
    def __neg__(self):
        'built-in -A support for integer'
        return integer(-self.output())
    
    def __add__(self, other):
        'built-in A+B support for integer'
        if not _operatable(other): return NotImplemented
        return integer(self.output() + integer(other).output())
    def __radd__(self, other):
        'built-in alternative A+B support for integer'
        return self + other
    
    def __sub__(self, other):
        'built-in A-B support for integer'
        if not _operatable(other): return NotImplemented
        return self + -other
    def __rsub__(self, other):
        'built-in alternative A-B support for integer'
        return -self + other
    
    def __mul__(self, other):
        'built-in A*B support for integer'
        if not _operatable(other): return NotImplemented
        return integer(self.output() * integer(other).output())
    def __rmul__(self, other):
        'built-in alternative A*B support for integer'
        return self * other
    
    def __floordiv__(self, other):
        'built-in A//B support for integer'
        if not _operatable(other): return NotImplemented
        return integer(self.output() // integer(other).output())
    def __rfloordiv__(self, other):
        'built-in A//B alternative support for integer'
        return integer(other) // self
    
    def __truediv__(self, other):
        'built-in A/B support for integer'
        if not _operatable(other): return NotImplemented
        if self % other == 0: return self // other
        return self.__frac__() / other # Call frac's division function if frac class is present
    'built-in A/B alternative support for integer'
    __rtruediv__ = lambda self, other: NotImplemented
    
    def __mod__(self, other):
        'built-in A%B support for integer'
        if not _operatable(other): return NotImplemented
        return integer(self.output() % integer(other).output())
    def __rmod__(self, other):
        'built-in A%B alternative support for integer'
        return integer(other) % self
    
    def __divmod__(self, other):
        'built-in divmod support for integer'
        if not _operatable(other): return NotImplemented
        return self // other, self % other
    def __rdivmod__(self, other):
        'builtin divmod alternative suppoort for integer'
        divmod(integer(other), self)
    
    def __pow__(self, other):
        'built-in A**B support for integer'
        if not _operatable(other): return NotImplemented
        if 0 != other % 1: return NotImplemented # for non-integer powers
        return integer(self.output() ** integer(other).output())
    def __rpow__(self, other):
        'builtin alternative A**B support for integer'
        return integer(other) ** self
    
    ## Conparison Operators
    def __eq__(self, other):
        'built-in A==B suppport for integer'
        if not _operatable(other): return NotImplemented
        return self.output() == integer(other).output()
    def __ne__(self, other):
        'built-in A!=B support for integer'
        return not (self == other)
    def __gt__(self, other):
        'built-in A>B support for integer'
        if not _operatable(other): return NotImplemented
        return self.output() > integer(other).output()
    def __ge__(self, other):
        'built-in A>=B support for integer'
        return not (self < other)
    def __lt__(self, other):
        'built-in A<B support for integer'
        if integer != type(other): return self < integer(other)
        return NotImplemented # force redirect
    def __le__(self, other):
        'built-in A<=B support for integer'
        if integer != type(other): return self <= integer(other)
        return NotImplemented # force redirect

def _operatable(arg):
    'take the argument itself'
    tpes = (
        # Builtin types
        int,
        float,
        str,
        # MI types
        integer,
    )
    return type(arg) in tpes
    

# TEST AREA
i1 = integer(2)
i2 = integer(3)
