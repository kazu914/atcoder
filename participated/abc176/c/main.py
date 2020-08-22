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
    a = LI()
    ans = 0
    for i in range(1, N):
        if a[i] >= a[i - 1]:
            continue
        ans += a[i - 1] - a[i]
        a[i] = a[i - 1]

    print(ans)


main()
