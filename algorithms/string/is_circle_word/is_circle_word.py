#!/usr/bin/env python

def is_circle_word(s1, s2):
    s_len = len(s1)
    if s_len != len(s2):
        return False

    try:
        s2_i = s2.index(s1[0])
    except ValueError:
        return False

    for s1_i in xrange(s_len):
        s2_ic = s2_i if s2_i < s_len else s2_i - s_len

        if s2[s2_ic] != s1[s1_i]:
            return False

        s2_i += 1

    return True


if __name__ == '__main__':
    n = int(raw_input())
    words = [raw_input().split(' ') for _ in xrange(n)]
    for item in words:
        print is_circle_word(*item)
