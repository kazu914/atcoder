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
    N = II()
    p = LI()

    ans = 0
    min_now = p[0]

    for i in range(N):
        if p[i] <= min_now:
            ans += 1
            min_now = p[i]

    print(ans)


main()
