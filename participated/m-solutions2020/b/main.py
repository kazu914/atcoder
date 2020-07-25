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
    a, b, c = MI()
    k = II()

    while k > 0:
        if a >= b:
            b *= 2
        elif b >= c:
            c *= 2

        k -= 1

    print("Yes" if c > b > a else "No")


main()
