#!/usr/bin/env python

import sys


def positives(a):
    return filter(lambda x: x > 0, a)


def negatives(a):
    return filter(lambda x: x < 0, a)


def zeros(a):
    return filter(lambda x: x == 0, a)


def count_plus_minus(a):
    p = n = z = 0
    for i in a:
        if i > 0:
            p += 1
        elif i < 0:
            n += 1
        else:
            z += 1
    return p, n, z


def percent_plus_minus(p, n, z):
    t = float(p + n + z)
    return (p / t), (n / t), (z / t)


if __name__ == '__main__':
    n = int(raw_input().strip())
    arr = map(int, raw_input().strip().split(' '))

    print '%.6f\n%.6f\n%.6f' % percent_plus_minus(*count_plus_minus(arr))
