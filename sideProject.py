#!/usr/bin/python3
# -*- encoding: utf8 -*-

from integer import integer

import pdb; t = pdb.set_trace

i = integer()

def iset(x):
    global i
    i = integer('1' * (3 ** x))

def get(x):
    return i / (3 ** x)

def test(x):
    k = 0
    try:
        while True:
            k += 1
            get(k)
    except: k -= 1
    finally: return k

def main():
    N = 50
    for ind in range(N):
        iset(ind)
        print('%s %s' % (ind, test(ind)))

if '__main__' == __name__: main()
