#!/usr/bin/env python


def sum_multiples_of(n, m):
    a = (n - 1) / m
    return m * ((a * (a + 1)) >> 1)


def sum_multiples_3_and_5(n):
    return sum_multiples_of(n, 3) + sum_multiples_of(n, 5) - sum_multiples_of(n, 15)


if __name__ == '__main__':
    l = int(raw_input().strip())
    for _ in xrange(l):
        n = int(raw_input().strip())
        print sum_multiples_3_and_5(n)
