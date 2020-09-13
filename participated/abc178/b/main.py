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
    a, b, c, d = MI()
    ans = -1 * 10 ** 19

    for A in [a, b]:
        for B in [c, d]:
            ans = max(ans, A * B)

    print(ans)


main()
