#!/usr/bin/env python

from collections import Counter


def ransom_note_v1(magazine, ransom):
    """Bad functions."""
    for w in ransom:
        if w not in magazine:
            return False
    return True


def ransom_note_v2(magazine, ransom):
    count = count_words(magazine)
    for w in ransom:
        if w in count and count[w] > 0:
            count[w] -= 1
        else:
            return False
    return True


def ransom_note_v3(magazine, ransom):
    return 0 == len(Counter(ransom) - Counter(magazine))


def count_words(words):
    count = {}
    for w in words:
        if w in count:
            count[w] += 1
        else:
            count[w] = 1
    return count


ransom_note = ransom_note_v3


if __name__ == '__main__':
    m, n = map(int, raw_input().strip().split())
    magazine = raw_input().strip().split()
    ransom = raw_input().strip().split()

    print 'Yes' if ransom_note(magazine, ransom) else 'No'
