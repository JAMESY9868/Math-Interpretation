#!/usr/bin/python3
# -*- encoding: utf8 -*-

from integer import *
from fraction import *
from decimal import *

from validation import *

from re import match
import mathRegex as mr

import pdb; t = pdb.set_trace

# Comp conversion
def _decFracComp(self):
    'decimal/frac to comp conversion'
    if not isType(self, (decimal, frac)): raise TypeError
    return comp((self, 0)).cpmode(self)

frac.__comp__ = _decFracComp
decimal.__comp__ = _decFracComp

class comp:
    def __init__(self, value = None):
        ''
        self.MODE = decimal
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
            elif tpe == str:
                if not match(expression, value): raise ValueError
                else: raise NotImplementedError
            elif ifIterable(value):
                if len(value) < 2: raise IndexError
                self.input([self.MODE(each) for each in value])
            elif not hasattr(value, '__comp__'): raise TypeError
            else: self.copy(value.__comp__())
    
    def __comp__(self):
        'comp conversion support'
        return self
    def __str__(self):
        'built-in str support for comp'
        re, im = self.output()
        reStr = str(re) # will always output the real part
        imStr = signStr(im, True) + ' ' + (
            str(abs(im)) + 'i' if decimal == self.MODE else # appended by imaginary part
            str(abs(im.output()[0])) + 'i/' + str(im.output()[1])
        )
        return reStr + ' ' + imStr
    def __repr__(self):
        'built-in repr support for comp'
        return str(self)
    
    def output(self):
        'output function'
        return tuple(self.value)
    def input(self, value):
        'input fuction'
        if not ifIterable(value): return self.copy(comp(value))
        elif len(value) < 2: raise IndexError
        self.value = [self.MODE(e) for e in value[:2]]
        return self
    def copy(self, other):
        'copy function'
        if not sameType(comp, self, other): raise TypeError
        return self.input(other.output())
    
    def remode(self, ifDecimal):
        'Change the internal info storage mode for comp, True for decimal and False for frac'
        if not isType(ifDecimal, (type, bool)): raise TypeError
        if isType(ifDecimal, type) and ifDecimal not in (decimal, frac): raise TypeError
        self.MODE = (
            (decimal if ifDecimal else frac) if isType(ifDecimal, bool) else ifDecimal
        )
        return self.copy(self)
    def cpmode(self, other):
        'Copy the internal info storage mode for comp from another comp instance'
        if not isType(other, (comp, decimal, frac)): raise TypeError
        if not isType(other, comp): return self.remode(type(other))
        return self.remode(other.MODE)
    
    def conj(self):
        'Conjugate of complex'
        return comp([
            sgn * self.output()[i]
            for i, sgn in zip(range(2), (1, -1))
        ]).cpmode(self)
    # Arithmetic Operations
    __unavail = lambda *_: NotImplemented # unavailable functions are drawn from here
    
    'Turn a complex number into a 2-element vector'
    makeVect = __unavail
    
    def __abs__(self):
        'built-in abs support for comp'
        vect = self.makeVect()
        return vect if NotImplemented == vect else abs(vect)
    
    def __pos__(self):
        'built-in +A support for comp'
        return self
    def __neg__(self):
        'built-in -A support for comp'
        return comp([
            -self.output()[i]
            for i in range(2)
        ]).cpmode(self)
    
    def __add__(self, other):
        'built-in A+B support for comp'
        if not _operatable(other): return NotImplemented
        return comp([
            self.output()[i] + comp(other).output()[i]
            for i in range(2)
        ]).cpmode(self)
    def __radd__(self, other):
        'built-in A+B alternative support for comp'
        return self + other
    
    def __sub__(self, other):
        'built-in A-B support for comp'
        if not _operatable(other): return NotImplemented
        return self + -other
    def __rsub__(self, other):
        'built-in A-B alternative support for comp'
        return -self + other
    
    def __mul__(self, other):
        'built-in A*B support for comp'
        if not _operatable(other): return NotImplemented
        return comp([
            self.output()[0] * other.output()[0] -
            self.output()[1] * other.output()[1],
            self.output()[0] * other.output()[1] +
            self.output()[1] * other.output()[0]
        ]).cpmode(self)
    def __rmul__(self, other):
        'built-in A*B alternative support for comp'
        return comp(other).cpmode(self) * self
    
    def __truediv__(self, other):
        'built-in A/B support for comp'
        if not _operatable(other): return NotImplemented
        other = comp(other)
        if 0 != other.output()[1]: return comp(
            (self * other.conj()) / (other * other.conj())
        ).cpmode(self)
        return comp([
            self.output()[i] / other.output()[0]
            for i in range(2)
        ]).cpmode(self)
    def __rtruediv__(self, other):
        'built-in A/B alternative support for comp'
        return comp(other).cpmode(self) / self
    
    'built-in A//B support for comp'
    __floordiv__ = __unavail
    'built-in A//B alternative support for comp'
    __rfloordiv__ = __unavail
    
    'built-in A%B support for comp'
    __mod__ = __unavail
    'built-in A%B alternative support for comp'
    __rmod__ = __unavail
    
    'built-in divmod support for comp'
    __divmod__ = __unavail
    'built-in divmod alternative support for comp'
    __rdivmod__ = __unavail
    
    # Comparison Operators
    def __eq__(self, other):
        'built-in A==B support for comp'
        if not _operatable(other): return NotImplemented
        return {True} == {
            m == n for m, n in zip(self.output(), comp(other).output())
        }
    def __ne__(self, other):
        'built-in A!=B support for comp'
        return not (self == other)
    
    'built-in A>B support for comp'
    __gt__ = __unavail
    'built-in A>=B support for comp'
    __ge__ = __unavail
    
    'built-in A<B support for comp'
    __lt__ = __unavail
    'built-in A<=B support for comp'
    __le__ = __unavail

def _operatable(arg):
    tpes = (
        int, 
        float,
        str,
        integer,
        frac,
        decimal,
        comp,
    )
    return type(arg) in tpes

c1 = comp((1, -2))
c2 = comp(('1.2_3', '9'))