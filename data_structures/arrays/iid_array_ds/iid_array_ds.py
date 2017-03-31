#!/usr/bin/env python

import sys


def print_arr(arr):
    for row in arr:
        print row
    print ''


def get_max_sandclock(arr):
    sums = []
    for pr in xrange(len(arr) - 2):
        for pc in xrange(len(arr) - 2):
            psum = 0
            for r in xrange(pr, pr + 3):
                for c in xrange(pc, pc + 3):
                    if r == pr + 1 and (c == pc or c == pc + 2):
                        continue
                    psum += arr[r][c]
            sums.append(psum)
    return max(sums)


if __name__ == '__main__':
    arr = []
    for arr_i in xrange(6):
        arr_temp = map(int, raw_input().strip().split(' '))
        arr.append(arr_temp)

    print get_max_sandclock(arr)
