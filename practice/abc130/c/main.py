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
    W, H, x, y = MI()
    ans = W * H / 2
    has_other = 1 if W / 2 == x and H / 2 == y else 0

    print(ans, has_other)


main()
