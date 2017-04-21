#!/usr/bin/env python

import sys
from math import floor


def median(l):
    l_sorted = sorted(l)
    # l_sorted = l
    # l_sorted.sort()
    l_len = len(l)
    i = int(floor(l_len / 2))
    if l_len % 2 == 0:
        return (l_sorted[i - 1] + l_sorted[i]) / 2.0
    else:
        return l_sorted[i]


def main():
    n = int(raw_input().strip())
    a = []
    a_i = 0
    for a_i in xrange(n):
        a_t = int(raw_input().strip())
        a.append(a_t)
        print '%.1f' % median(a)


if __name__ == '__main__':
    main()
