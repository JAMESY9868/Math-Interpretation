#!/usr/bin/python3
# -*- encoding: utf8 -*-

'''
Current idea is to use an int to represent the number
with customized methods connecting to other objects
'''
from re import match

# Debugging Tools
import pdb
t = pdb.set_trace

class integer:
    '''
    .value: int
    '''
    def __init__(self, value = None):
        if value is not None:
        # Conversion init
            try:
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
                elif '__integer__' not in dir(value): raise TypeError
                else: self.input(value.__integer__().value)
                return
            except:
                print('Placeholder error messege')
        # Default init
        self.value = 0
    def __integer__(self):
        'support for integer constructor'
        return self
    def output(self):
        'The output function for integer'
        return self.value
    def input(self, value):
        'the input function for integer'
        if DEFAULT_TYPE != type(value): return self.input(_THIS_CLASS(value).output())
        self.value = value
        return self
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
    def __repr__(self):
        'built-in repr support for integer'
        return str(self)
    def __abs__(self):
        'built-in abs support for integer'
        return abs(self.value)
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
        return self.value // o.value
    def __truediv__(self, other):
        'built-in A/B support for integer'
        o = integer(other) # thus filter out weird inputs
        return self.value / o.value
    def __mod__(self, other):
        'built-in A%B support for integer'
        o = integer(other) # thus filter out weird inputs
        return self.value % o.value
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

def _isInt(num):
    types = [
        int,
        str,
        integer,
    ]
    if type(num) not in types: return False
    expression = '^-?\d+$'
    if str == type(num):
        if not match(expression, num): return False
    return True

def _intCheck(num):
    if not _isInt(num): raise TypeError

DEFAULT_TYPE = int # the default type of value
_THIS_CLASS = integer # this class

# IF USING THE TEST AREA
testing = True

if testing:
    # TEST AREA
    i1 = integer(2)
    i2 = integer(3)
    mode = 3
    i = (
        i1 + i2 if 1 == mode else
        i1 - i2 if 2 == mode else
        i1 * i2 if 3 == mode else
        i1 / i2 if 4 == mode else
        i1 % i2
    )
    print('%s %s %s = %s'%(i1, '+-*/%'[mode - 1], i2, i))
pass
