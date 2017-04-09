#!/usr/bin/env python

def array_left_rotation(a, n, k):
    o = []
    append = o.append
    for i in xrange(k, k + n):
        j = i - n if i >= n else i
        append(a[j])
    return o

if __name__ == '__main__':
    n, k = map(int, raw_input().strip().split())
    a = map(int, raw_input().strip().split())
    print ' '.join(map(str, array_left_rotation(a, n, k)))
