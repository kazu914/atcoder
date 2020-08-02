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
    a, b, n = MI()
    ans = 0
    if n < b:
        ans = (a * n) // b
    else:
        ans = (a * (b - 1)) // b

    print(ans)


main()
