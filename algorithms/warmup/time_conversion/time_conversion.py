#!/usr/bin/env python


def time_conversion(input_time):
    """Conversion AM/PM to military hours."""
    a = input_time.split(':')
    a[2], m = a[2][:2], a[2][2:]
    a = map(int, a)

    if 'PM' == m:
        a[0] = a[0] + 12 if a[0] < 12 else a[0]
    else:
        a[0] = 0 if a[0] == 12 else a[0]

    return '%02d:%02d:%02d' % tuple(a)


if __name__ == '__main__':
    print time_conversion(raw_input().strip())
