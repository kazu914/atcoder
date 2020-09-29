#!/usr/bin/env python3
import collections as cl
import sys


def II():
    return int(sys.stdin.readline())


def MI():
    return map(int, sys.stdin.readline().split())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def main():
    s = input()

    l, r = 0, len(s) - 1
    x_l, x_r = 0, 0

    while l <= r:
        if s[l] == s[r]:
            l += 1
            r -= 1
            continue
        if s[l] == 'x':
            l += 1
            x_l += 1
            continue
        if s[r] == 'x':
            r -= 1
            x_r += 1
            continue
        print(-1)
        return

    print(x_l + x_r)


main()
