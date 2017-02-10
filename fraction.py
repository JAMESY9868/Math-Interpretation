#!/usr/bin/python3
# -*- encoding: utf8 -*-

from re import match
from integer import integer

# Debugging Tools
import pdb
t = pdb.set_trace

class frac:
    def __init__(self, value = None):
        # Conversion init
        try:
            if value is not None:
                # check if value is of primative types such as int
                tpe = type(value)
                builtins = [
                    int,
                    float,
                    str,
                ]
                # Deal with currently supported types, others raise exception
                if int == tpe: self.input(value, 1)
                elif tpe in builtins: raise NotImplementedError
                # then check if __integer__ available
                elif '__frac__' not in dir(value): raise TypeError
                else: self.input(*value.__frac__().output())
                return
        except: print('Placeholder error messege')
        # Default init
        self.input(0, 1)
    def __frac__(self):
        'Conversion support frac -> frac'
        return self
    def output(self):
        'Return a tuple consisting of both the numerator and the denominator'
        return self.numer, self.denom 
    def input(self, numer, denom):
        'Check validity of input set and assign'
        self.inputRaw(numer, denom)
        self.simplify()
        return self
    def inputRaw(self, numer, denom):
        'Check validity of input set and assign'
        # Checking section
        if not (_isNum(numer) or _isNum(denom)): raise TypeError(
                'The arguments provided cannot be interpreted as numbers. Please try other combinations.'
        )
        if _isZero(denom): raise ValueError(
            'The denominator cannot be 0. Please try other values. '
        )
        # Assignment section
        self.numer = str(numer)
        self.denom = str(denom)
        # Return self
        return self
    def simplify(self):
        'Simplify the fraction'
        # Not yet implemented
        return self
    def str(self):
        'Needs more work here, get the string version of fraction'
        # Needs to remove parentheses in unnecessary cases
        return '(%s)/(%s)' % self.output()
    def inv(self):
        'Inverse the fraction FLAG: LIMIT'
        _zeroCheck(self, 'Cannot invert 0.')
        return frac().input(*(self.output()[::-1]))
    def sign(self):
        'Return a bool of the sign, with the understanding that 0 => pos FLAG: NON-EXPR-COMPATIBLE'
        return sign(self)
    def __sign__(self):
        'add support for global sign()'
        return sign(integer(self.numer) * self.denom)
    def __str__(self):
        'built-in str() support for frac'
        return self.str()
    def __abs__(self):
        'built-in abs() support for frac'
        return -self if self.sign() < 0 else self
    def __pos__(self):
        'built-in +A support for frac'
        return self
    def __neg__(self):
        'built-in -A support for frac'
        return frac().input(-integer(self.numer), self.denom)
    def __add__(self, other):
        'built-in A+B support for frac'
        # First known that 'self' is of type frac
        # Then ensure that 'other' is a number (thus "add-able", same for other basic operations)
        _numCheck(other)
        # temp vars
        o = frac(other)
        a, b, c, d = [
            integer(e) for e in self.output() + o.output()
        ]
        # Return result
        # a/b + c/d = (ad+bc)/(bd)
        return frac().input(a * d + b * c, b * d)
    def __sub__(self, other):
        'built-in A-B support for frac'
        # First known that 'self' is of type frac
        # Then ensure that 'other' is a number
        if not _isNum(other): raise TypeError
        # Return result
        return self + -other
    def __mul__(self, other):
        'built-in A*B support for frac'
        # First known that 'self' is of type frac
        # Then ensure that 'other' is a number
        if not _isNum(other): raise TypeError
        # temp vars
        o = frac(other)
        a, b, c, d = [
            integer(e) for e in self.output() + o.output()
        ]
        # Return result
        # a/b * c/d = (ac)/(bd)
        return frac().input(a * c, b * d)
    def __floordiv__(self, other):
        'built-in A//B support for frac, return integer FLAG: EXPR'
        # Placeholder only
        trueDiv = self / other
        if trueDiv < 0: return -(-trueDiv) // 1 - 1
        elif trueDiv == 0: return integer(0)
        return integer(trueDiv.numer) // trueDiv.denom
    def __truediv__(self, other):
        'built-in A/B support for frac FLAG: LIMIT'
        # First known that 'self' is of type frac
        # Then ensure that 'other' is a number
        _numCheck(other)
        # Return result
        _zeroCheck(other, 'Cannot divide by 0')
        o = frac(other)
        return self * o.inv()
    def __mod__(self, other):
        'built-in A%B support for frac FLAG: NO-LIMIT'
        # First known that 'self' is of type frac
        # Then ensure that 'other' is a number
        _numCheck(other)
        _zeroCheck(other, 'Cannot divide by 0')
        return self - other * (self // other)
    ## Conparison Operators
    def __eq__(self, other):
        'built-in A==B support for frac'
        # First known that 'self' is of type frac
        # Then ensure that 'other' is a number
        _numCheck(other)
        selfSim = self.simplify()
        otherSim = frac(other).simplify()
        return selfSim.output() == otherSim.output()
    def __ne__(self, other):
        'built-in A!=B support for frac'
        # First known that 'self' is of type frac
        # Then ensure that 'other' is a number
        _numCheck(other)
        return not (self == other)
    def __gt__(self, other):
        'built-in A>B support for frac FLAG: EXPR'
        if type(other) != frac: return self > frac(other)
        ss, so = [e.sign() for e in (self, other)]
        if ss != so: return ss > so
        if ss < 0: return -self < -other
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
        
pass # Placed for ease of using the editor, no real purpose

def _isNum(num):
    '''
    Checks if the input is of one of the following types
        int
        str containing ONLY int
    return the decision
    '''
    types = [
        int,
        str,
        frac,
        integer,
    ]
    if type(num) not in types: return False
    # check by type
    strMatch = '^\d*$' # only integers right now
    if str == type(num):
        if not match(strMatch, num):
            return False
    return True

def _isZero(arg):
    'integer section needs changed'
    tpe = type(arg)
    if tpe in [
        int, float,
    ]:
        return arg == 0
    elif tpe == str:
        return not [i for i in arg if i != '0']
    elif tpe == frac:
        return _isZero(arg.numer)
    elif tpe == integer:
        return _isZero(arg.value)
    else:
        raise NotImplementedError

def _numCheck(num):
    'A fast way of checking if an input is a number'
    if not _isNum(num): raise TypeError
def _zeroCheck(num, messege = ''):
    'A fast way of checking if a number is 0'
    if _isZero(num): raise ValueError(messege)

DEFAULT_TYPE = integer # the default type of numerator and denominator, NOT IMPLEMENTED YET
_THIS_CLASS = frac

# IF USING THE TEST AREA
testing = False

if testing:
    # TEST AREA
    f1 = frac().input(1, 8)
    f2 = frac().input(3, 4)
    mode = 5 # subtraction
    f = (
        f1 + f2 if 1 == mode else
        f1 - f2 if 2 == mode else
        f1 * f2 if 3 == mode else
        f1 / f2 if 4 == mode else
        f1 % f2
    )
    print('(%s) %s (%s) = %s'%(f1, '+-*/%'[mode - 1], f2, f))

pass