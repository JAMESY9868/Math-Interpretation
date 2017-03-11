#!/usr/bin/python3
# -*- encoding: utf8 -*-

Prototype='';function='';alternative='';support='';built=''

class scalar:
    'This is a prototype class'
    # Defines all the properties and methods for a scalar.
    __unavail = lambda *_, **__: NotImplemented
    __done = lambda *_, **__: None
    
    'Prototype constructor'
    __init__ = __done
    'Prototype input function'
    input = __done
    'Prototype output function'
    output = __done
    
    # Arithmetic Operators
    'Prototype built-in abs support for scalar'
    __abs__ = __unavail
    'Prototype built-in +A support for scalar'
    __pos__ = __unavail
    'Prototype built-in -A support for scalar'
    __neg__ = __unavail
    
    'Prototype built-in A+B support for scalar'
    __add__ = __unavail
    'Prototype built-in A+B alternative support for scalar'
    __radd__ = __unavail
    
    'Prototype built-in A-B support for scalar'
    __sub__ = __unavail
    'Prototype built-in A-B alternative support for scalar'
    __rsub__ = __unavail
    
    'Prototype built-in A*B support for scalar'
    __mul__ = __unavail
    'Prototype built-in A*B alternative support for scalar'
    __rmul__ = __unavail
    
    'Prototype built-in A/B support for scalar'
    __truediv__ = __unavail
    'Prototype built-in A/B alternative support for scalar'
    __rtruediv__ = __unavail
    
    'Prototype built-in A//B support for scalar'
    __floordiv__ = __unavail
    'Prototype built-in A//B alternative support for scalar'
    __rfloordiv__ = __unavail
    
    'Prototype built-in A%B support for scalar'
    __mod__ = __unavail
    'Prototype built-in A%B alternative support for scalar'
    __rmod__ = __unavail
    
    'Prototype built-in divmod support for scalar'
    __divmod__ = __unavail
    'Prototype built-in divmod alternative support for scalar'
    __rdivmod__ = __unavail
    
    # Comparison Operators
    'Prototype built-in A==B support for scalar'
    __eq__ = __unavail
    'Prototype built-in A!=B support for scalar'
    __ne__ = __unavail
    
    'Prototype built-in A>B support for scalar'
    __gt__ = __unavail
    'Prototype built-in A>=B support for scalar'
    __ge__ = __unavail
    
    'Prototype built-in A<B support for scalar'
    __lt__ = __unavail
    'Prototype built-in A<=B support for scalar'
    __le__ = __unavail