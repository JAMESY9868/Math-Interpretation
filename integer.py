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
        if not (type(self) == integer == type(other)): raise TypeError
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
    def sign(self):
        'sign of integer'
        return sign(self)
    def __sign__(self):
        'add support for global sign()'
        return integer(
            1 if self.output() > 0 else
            -1 if self.output() < 0 else
            0
        )
    def str(self):
        'get the string version of integer'
        return str(self)
    def __str__(self):
        'built-in str support for integer'
        # placeholder
        return str(self.output())
    def __repr__(self):
        'built-in repr support for integer'
        return str(self)
    def __int__(self):
        'built-in int support for integer'
        return self.output()
    def __repr__(self):
        'built-in repr support for integer'
        return str(self)
    def __abs__(self):
        'built-in abs support for integer'
        return integer(abs(self.output()))
    def __neg__(self):
        'built-in -A support for integer'
        # placeholder
        return integer(-self.output())
    def __add__(self, other):
        'built-in A+B support for integer'
        return integer(self.output() + other.output())
    def __radd__(self, other):
        'built-in alternative A+B support for integer'
        return self + other
    def __sub__(self, other):
        'built-in A-B support for integer'
        return self + -other
    def __rsub__(self, other):
        'built-in alternative A-B support for integer'
        return -self + other
    def __mul__(self, other):
        'built-in A*B support for integer'
        return integer(self.output() * o.output())
    def __rmul__(self, other):
        'built-in alternative A*B support for integer'
        return self * other
    def __pow__(self, other):
        'built-in A**B support for integer'
        tpe = type(other)
        if integer == tpe: return integer(self.output() ** other.output())
        builtins = [
            int,
            str,
        ]
        if type(other) not in builtins:
            if 0 != other % 1: return NotImplemented
        return self ** integer(other)
    
    def __rpow__(self, other):
        'builtin alternative A**B support for integer'
        return integer(other) ** self
    
    def __rmul__(self, other):
        'built-in A*B alternative support for integer'
        return self * other
    def __divmod__(self, other):
        'built-in divmod support for integer'
        return self // other, self % other
    def __floordiv__(self, other):
        'built-in A//B support for integer'
        o = integer(other) # thus filter out weird inputs
        return integer(self.output() // o.output())
    def __truediv__(self, other):
        'built-in A/B support for integer'
        if self % other == 0: return self // other
        raise NotImplementedError(
            'Needs to import fraction module'
        )
    def __mod__(self, other):
        'built-in A%B support for integer'
        o = integer(other) # thus filter out weird inputs
        return self - o * (self // o)
    ## Conparison Operators
    def __eq__(self, other):
        'built-in A==B suppport for integer'
        return self.output() == other.output()
    def __ne__(self, other):
        'built-in A!=B support for integer'
        o = integer(other) # thus filter out weird inputs
        return not (self == other)
    def __gt__(self, other):
        'built-in A>B support for integer'
        o = integer(other) # thus filter out weird inputs
        return self.output() > o.output()
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
pass # placeholder, no purpose

# TEST AREA
i1 = integer(2)
i2 = integer(3)
