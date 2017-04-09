#!/usr/bin/env python

from collections import Counter


def number_needed_v1(a, b):
    """Number needed use set functions."""
    aset = set(a)
    bset = set(b)
    return len(aset.symmetric_difference(bset))


def number_needed_v2(a, b):
    return delete_count(a, b) + delete_count(b, a)


def number_needed_v3(a, b):
    acounter = Counter(a)
    bcounter = Counter(b)
    acounter.subtract(b)
    return sum(abs(i) for i in acounter.itervalues())


def number_needed_v4(a, b):
    afreq = frequency(a)
    bfreq = frequency(b)
    return sum(abs(i) for i in subtract_frequency(afreq, bfreq).itervalues())


def delete_index(a, b):
    return [i for i in xrange(len(a)) if a[i] not in b]


def delete_index_generator(a, b):
    for i in xrange(len(a)):
        if a[i] not in b:
            yield i


def delete_chars(a, b):
    return [c for c in a if c not in b]


def delete_chars_generator(a, b):
    for c in a:
        if c not in b:
            yield c


def delete_count(a, b):
    count = 0
    for c in a:
        if c not in b:
            count += 1
    return count

def frequency(a):
    count = {}
    for c in a:
        if c in count.keys():
            count[c] += 1
        else:
            count[c] = 1
    return count


def subtract_frequency(a, b):
    o = dict(a)
    for c in b.iterkeys():
        if c in o:
            o[c] -= b[c]
        else:
            o[c] = -b[c]
    return o


number_needed = number_needed_v4


if __name__ == '__main__':
    a = raw_input().strip()
    b = raw_input().strip()
    print number_needed(a, b)
