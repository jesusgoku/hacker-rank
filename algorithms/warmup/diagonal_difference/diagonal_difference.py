#!/usr/bin/env python

import sys


def diagonal_primary(a):
    return [a[i][i] for i in xrange(len(a))]


def diagonal_secondary(a):
    return [a[i][len(a) - i - 1] for i in xrange(len(a))]


def diagonal_difference(a):
    return sum(diagonal_primary(a)) - sum(diagonal_secondary(a))


if __name__ == '__main__':
    n = int(raw_input().strip())
    a = []
    for a_i in xrange(n):
        a_temp = map(int, raw_input().strip().split(' '))
        a.append(a_temp)

    print abs(diagonal_difference(a))
