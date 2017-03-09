#!/usr/bin/python3
# -*- encoding: utf8 -*-

from globalFunc import *
from validation import *

from complex import *

class vector():
    def __init__(self, value = None):
        ''
        self.input((0,))
        if value is not None:
            if not ifIterable(value): raise NotImplementedError
            if hasattr(value, '__vector__'): self.copy(other.__vector__())
            else: self.input(value)
    def __vector__(self):
        'support for vector'
        return self
    
    def __str__(self):
        'built-in str support for vector'
        return 'vector(%s)' % (self.output(),)
    def __repr__(self):
        'built-in repr support for vector'
        return str(self)
    def __iter__(self):
        'built-in iter support for vector'
        return iter(self.output()) # for now, probably needs modification
    def __getitem__(self, ind):
        'built-in A[B] support for vector'
        return self.output()[ind]
    
    def output(self):
        return self.value
    def input(self, value):
        ''
        if not ifIterable(value): raise NotImplementedError
        if {True} != {_operatable(e) for e in value}: raise TypeError
        self.value = [comp(e) for e in value]
    def copy(self, other):
        ''
        pass
    
    def normalize(self):
        ''
        return self / sum(self)
    
    def __len__(self):
        'built-in len support for vector'
        return len(self.output())
    def __size__(self):
        'globalFunc size support for vector'
        return len(self)
    
    def dot(self, other):
        'support for dotting multiplication'
        return sum((self * other).output()) # might need modification
    def cross(self, other):
        'support for cross multiplication'
        raise NotImplementedError
    
    # Arithmetic Operation (Entry-wise Operations)
    def __abs__(self):
        'built-in abs support for vector NOTE: abs in this case returns sqrt(sum(e**2 for e in self))'
        raise NotImplementedError
    def __pos__(self):
        'built-in +A support for vector'
        return self
    def __neg__(self):
        'built-in -A support for vector'
        return vector([-e for e in self.output()])
    
    def __add__(self, other):
        'built-in A+B support for vector'
        if not sameType(vector, self, other): raise TypeError
        if size(self) != size(other): raise ValueError
        return foreach(lambda a,b:a+b, self, other)
    def __radd__(self, other):
        'built-in A+B alternative support for vector'
        return self + other
    
    def __sub__(self, other):
        'built-in A-B support for vector'
        return self + -other
    def __rsub__(self, other):
        'built-in A-B alternative support for vector'
        return -self + other
    
    def __mul__(self, other):
        'built-in A*B support for vector'
        if _operatable(other): return foreach(lambda a: a * other, self)
        if not sameType(vector, self, other): return NotImplemented
        if size(self) != size(other): raise ValueError
        return foreach(lambda a,b:a*b, self, other)
    def __rmul__(self, other):
        'built-in A*B alternative support for vector'
        return self * other
    
    def __floordiv__(self, other):
        'built-in A//B support for vector'
        if _operatable(other): return foreach(lambda a: a // other, self)
        if not sameType(vector, self, other): return NotImplemented
        if size(self) != size(other): raise ValueError
        return foreach(lambda a,b:a//b, self, other)
        # This will for now / ever raise TypeError because there is no meaning found for comp // comp. Ideas?
    def __rfloordiv__(self, other):
        'built-in A//B alternative support for vector'
        return 
    
    def __truediv__(self, other):
        'built-in A/B support for vector'
        if _operatable(other): return foreach(lambda a: a / other, self)
        if not sameType(vector, self, other): return NotImplemented
        if size(self) != size(other): raise ValueError
        return foreach(lambda a,b:a/b, self, other)
    
    def __mod__(self, other):
        'built-in A%B support for vector'
        if not sameType(vector, self, other): return NotImplemented
        if size(self) != size(other): raise ValueError
        return foreach(lambda a,b:a%b, self, other)
        # TypeError. Refer to __floordiv__
    
    def __divmod__(self, other):
        'built-in divmod support for vector'
        if not sameType(vector, self, other): return NotImplemented
        if size(self) != size(other): raise ValueError
        return foreach(divmod, self, other)
        # TypeError. Refer to __floordiv__
    
def dot(first, second):
    'global dot multiplication function'
    return first.dot(second)

def cross(first, second):
    'global cross multiplication function'
    return first.cross(second)

def foreach(func, *vects):
    'entry-wise function performance'
    if not ifIterable(vects[0]): raise TypeError
    if ifIterable(vects[0][0]): return foreach(*(vects[0]))
    reqLen, argLen = func.__code__.co_argcount, len(vects)
    vects = (
        vects if reqLen == argLen else
        (vects + ((),) * (len(vects) - reqLen)) if reqLen < argLen else
        vects[:argLen]
    )
    return vector([func(*e) for e in zip(*vects)])

def _operatable(arg):
    ''
    tpes = (
        # for single element
        int,
        float,
        str,
        integer,
        frac,
        decimal,
        comp,
    )
    return type(arg) in tpes

v1 = vector((2, 3, 4))
v2 = vector((-2, f2, 7))
