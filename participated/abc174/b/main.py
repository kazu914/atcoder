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
    n, d = MI()
    ans = 0
    for i in range(n):
        x, y = MI()
        if x ** 2 + y ** 2 <= d ** 2:
            ans += 1

    print(ans)


main()
