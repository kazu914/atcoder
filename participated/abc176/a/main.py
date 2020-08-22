#!/usr/bin/env python3
import collections as cl
import sys

import math


def II():
    return int(sys.stdin.readline())


def MI():
    return map(int, sys.stdin.readline().split())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def main():
    n, x, t = MI()

    print(math.ceil(n / x) * t)


main()
