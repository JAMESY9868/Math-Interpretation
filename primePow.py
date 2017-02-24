#!/usr/bin/python3
# -*- encoding: utf8 -*-

from integer import *

def primePow(base, divisor):
    '''
    b <= base; d <= divisor
    b = (d ** N) * b_0, where b_0 is not divisible by d
    This function determines the N value
    '''
    return _primePow(integer(base), integer(divisor))

def _primePow(baseInt, divisorInt):
    'Refer to primePow(), implying integer type'
    if 0 != (baseInt % divisorInt): return 0
    return 1 + _primePow(baseInt / divisorInt, divisorInt)
