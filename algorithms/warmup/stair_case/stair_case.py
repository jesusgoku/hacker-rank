#!/usr/bin/env python


def stair_case(n):
    for row in xrange(n):
        colstr = ''
        for col in xrange(n):
            colstr += '#' if col >= (n - 1 - row) else ' '
        print colstr


if __name__ == '__main__':
    stair_case(int(raw_input()))
