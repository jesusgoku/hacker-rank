#!/usr/bin/env python


INVERSE = {
    ')': '(',
    ']': '[',
    '}': '{'
}


def is_matched(expr):
    st = []
    for c in expr:
        if c in INVERSE:
            if 0 == len(st) or INVERSE[c] != st.pop():
                return False
        else:
            st.append(c)

    return True if 0 == len(st) else False


if __name__ == '__main__':
    n = int(raw_input().strip())
    for _ in xrange(n):
        expression = raw_input().strip()
        print 'YES' if is_matched(expression) else 'NO'
