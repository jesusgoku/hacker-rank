#!/usr/bin/env python
"""HackerRank excerices of algorithms.
Algorithms  Greedy  Max Min
https://www.hackerrank.com/challenges/angry-children
"""


def main():
    N = input()
    K = input()
    lists = [input() for _ in xrange(0, N)]
    lists.sort()

    print min_diff(N, K, lists)


def min_diff_v1(N, K, lists):
    i = 0
    j = N - K
    diffs = []
    append = diffs.append

    while i <= j:
        # plist = lists[i:(i + K)]
        # append(plist[-1] - plist[0])
        append(lists[i + K - 1] - lists[i])
        i += 1

    return min(diffs)


def min_diff_v2(N, K, lists):
    """An integer that denotes the minimum possible value of unfairness.

    :param N: Long of list
    :param K: Size subgroups
    :param lists: List of integers
    """
    return min(map(lambda i: lists[(i + K - 1)] - lists[i], xrange(N - K + 1)))


min_diff = min_diff_v1


if __name__ == '__main__':
    main()
