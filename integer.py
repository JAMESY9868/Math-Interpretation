#!/usr/bin/python3
# -*- encoding: utf8 -*-

from re import match

class integer:
    def __init__(self, value = 0):
        try: self.setValue(value)
        except:
            1/0 # placeholder for printing the original error
            self.value = 0
    def setValue(self, value):
        if not _isInt(value): raise TypeError(
            'The argument provided cannot be interpreted as an integer. '
        )
        self.value = value
        # placeholder for dealing with this number
        self.value = int(self.value)
        return self
    @staticmethod
    def parseStr(strInt):
        '###'
        return integer(int(strInt))
    def sign(self):
        'sign of integer'
        if self.value > 0: return integer(1)
        if self.value < 0: return integer(-1)
        return integer(0)
    def __abs__(self):
        'built-in abs support for integer'
        raise NotImplementedError
    def __str__(self):
        'built-in str support for integer'
        # placeholder
        return str(self.value)
    def __neg__(self):
        'built-in -A support for integer'
        # placeholder
        return integer(-self.value)
    def __add__(self, other):
        'built-in A+B support for integer'
        # placeholder
        return integer().setValue(self.value + other.value)
    def __mul__(self, other):
        'built-in A*B support for integer'
        # placeholder
        return integer().setValue(self.value * other.value)
    def __floordiv__(self, other):
        'built-in A//B support for integer'
        pass
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
