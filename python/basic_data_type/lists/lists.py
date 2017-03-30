#!/usr/bin/env python


def main():
    N = int(raw_input())

    l = []
    for i in xrange(N):
        process(l, raw_input())


def process(l, input_raw):
    input_data = input_raw.split(' ')

    action = input_data[0]

    if 'insert' == action:
        linsert(l, input_data[1], input_data[2])
    elif 'print' == action:
        lprint(l)
    elif 'remove' == action:
        lremove(l, input_data[1])
    elif 'sort' == action:
        lsort(l)
    elif 'pop' == action:
        lpop(l)
    elif 'reverse' == action:
        lreverse(l)
    elif 'append' == action:
        lappend(l, input_data[1])


def linsert(l, pos, value):
    l.insert(int(pos), int(value))


def lprint(l):
    print l


def lremove(l, value):
    del l[l.index(int(value))]


def lsort(l):
    l.sort()


def lpop(l):
    l.pop()


def lreverse(l):
    l.reverse()


def lappend(l, value):
    l.append(int(value))


if __name__ == '__main__':
    main()
