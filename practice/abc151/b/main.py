#!/usr/bin/env python3
import collections as cl
import math
import sys


def II():
    return int(sys.stdin.readline())


def MI():
    return map(int, sys.stdin.readline().split())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def main():
    n, k, m = MI()

    a = LI()
    rest = max(math.ceil(m * n - sum(a)), 0)

    print(-1 if rest > k else rest)


main()
