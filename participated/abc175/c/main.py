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
    x, k, d = MI()
    x = abs(x)

    min_idou = x // d
    amari = x % d

    if min_idou >= k:
        print(min(abs(x - k*d), x))
        return

    k -= min_idou
    if k % 2 == 0:
        print(amari)
    else:
        print(-1*(amari - d))


main()
