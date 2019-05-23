#!/usr/bin/env python
# -*-coding: utf-8 -*-


def hannoi(n, a, b, c):
    count = 0
    if n == 1:
        print('%s -> %s' % (a, c))
        return 1
    else:
        count += hannoi((n-1), a, c, b)
        count += hannoi(1, a, b, c)
        count += hannoi((n-1), b, a, c)
        return count

count = hannoi(64, 'A', 'B', 'C')
print(count)