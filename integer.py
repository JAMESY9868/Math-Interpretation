#!/usr/bin/python3
# -*- encoding: utf8 -*-

#
# Current idea is to use an int to represent the number
# with customized methods connecting to other objects
#

from globalFunc import *

from re import match

# Debugging Tools
import pdb
t = pdb.set_trace

_DEFAULT_TYPE = int # the default type of value held inside the class

class integer:
    '''
    .value: int
    '''
    def __init__(self, value = None):
        # Default init
        self.value = 0
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
            elif str == tpe: self.input(int(value))
            elif tpe in builtins: raise NotImplementedError
            # then check if __integer__ available
            elif not hasattr(value, '__integer__'): raise TypeError
            else: self.input(value.__integer__().value)
            return
    def __integer__(self):
        'support for integer constructor'
        return self
    def output(self):
        'The output function for integer'
        return self.value
    def input(self, value):
        'the input function for integer'
        if _DEFAULT_TYPE != type(value): return self.input(integer(value).output())
        self.value = value
        return self
    def copy(self, other):
        'copy function'
        # strict same type
        if type(self) != integer != type(other): raise TypeError
        return self.input(other.output())
    def setValue(self, value):
        raise DeprecationWarning
        raise Exception
        if not _isInt(value): raise TypeError(
            'The argument provided cannot be interpreted as an integer. '
        )
        self.value = value
        # placeholder for dealing with this number
        self.value = int(self.value)
        return self
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
            1 if self.value > 0 else
            -1 if self.value < 0 else
            0
        )
    def str(self):
        'get the string version of integer'
        return str(self)
    def __str__(self):
        'built-in str support for integer'
        # placeholder
        return str(self.value)
    def __int__(self):
        'built-in int support for integer'
        return self.output()
    def __repr__(self):
        'built-in repr support for integer'
        return str(self)
    def __abs__(self):
        'built-in abs support for integer'
        return integer(abs(self.value))
    def __neg__(self):
        'built-in -A support for integer'
        # placeholder
        return integer(-self.value)
    def __add__(self, other):
        'built-in A+B support for integer'
        o = integer(other) # thus filter out weird inputs
        return integer(self.value + o.value)
    def __sub__(self, other):
        'built-in A-B support for integer'
        o = integer(other) # thus filter out weird inputs
        return self + -o
    def __mul__(self, other):
        'built-in A*B support for integer'
        o = integer(other) # thus filter out weird inputs
        return integer(self.value * o.value)
    def __floordiv__(self, other):
        'built-in A//B support for integer'
        o = integer(other) # thus filter out weird inputs
        return integer(self.value // o.value)
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
        o = integer(other) # thus filter out weird inputs
        return self.value == o.value
    def __ne__(self, other):
        'built-in A!=B support for integer'
        o = integer(other) # thus filter out weird inputs
        return not (self == other)
    def __gt__(self, other):
        'built-in A>B support for integer'
        o = integer(other) # thus filter out weird inputs
        return self.value > o.value
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
mode = 3

