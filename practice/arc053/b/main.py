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
    S = input()
    count = cl.Counter()

    for s in S:
        count.update({s: 1})

    base = 0
    others = 0

    for k, v in count.items():
        base += v % 2
        others += v - v % 2

    if base == 0:
        print(base + others)
        return

    min_div = math.floor((others / 2) / base)
    print(min_div*2 + 1)


main()
