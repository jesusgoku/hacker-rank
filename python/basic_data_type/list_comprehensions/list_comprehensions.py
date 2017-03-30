#!/usr/bin/env python


def list_comprehensions(x, y, z, n):
    return sorted([[i, j, k] for k in xrange(z + 1)
                  for j in xrange(y + 1)
                  for i in xrange(x + 1)
                  if i + j + k != n])


if __name__ == '__main__':
    x = int(raw_input())
    y = int(raw_input())
    z = int(raw_input())
    n = int(raw_input())
    print list_comprehensions(x, y, z, n)
