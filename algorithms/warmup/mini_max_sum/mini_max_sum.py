#!/usr/bin/env python


def mini_max_sum(a):
    sums = []
    a_length = len(a)
    for i in xrange(a_length):
        sum = 0
        for j in xrange(i, i + a_length - 1):
            index = j - a_length if j >= a_length else j
            sum += a[index]
        sums.append(sum)
    return min(sums), max(sums)


if __name__ == '__main__':
    a = map(int, raw_input().strip().split(' '))

    print '%d %d' % mini_max_sum(a)
