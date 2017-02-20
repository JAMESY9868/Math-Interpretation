#!/usr/bin/python3
# -*- encoding: utf8 -*-

from integer import *
from fraction import *
from decimal import *

from validation import *

from re import match
import mathRegex as mr

_DEFAULT_TYPE = decimal

class comp:
    def __init__(self, value = None):
        ''
        # Default init
        self.input((0, 0))
        # Conversion init
        if value is not None:
            tpe = type(value)
            builtins = [
                int,
                float,
                str,
            ]
            expression = mr.full(mr.COMPLEX)
            if tpe in (int, float): self.__init__((value, 0)) # recursive constructor
            if tpe == str:
                if not match(expression, value): raise ValueError
                else: raise NotImplementedError
            if ifIterable(value):
                if len(value) < 2: raise IndexError
                self.input([_DEFAULT_TYPE(each) for each in value])
            if not hasattr(value, '__comp__'): raise TypeError
            self.copy(value.__comp__())
    def output(self):
        'output function'
        return tuple(self.value)
    def input(self, value):
        'input fuction'
        if not ifIterable(value): return self.copy(comp(value))
        
    def copy(self, other):
        'copy function'
        if type(self) != comp != type(other): raise TypeError
        self.input(other.output())