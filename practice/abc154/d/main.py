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
    n, k = MI()
    p = LI()
    max_seq = sum(p[:k])

    current = sum(p[:k])

    for i in range(k, n):
        current = current - p[i - k] + p[i]
        max_seq = max(max_seq, current)

    print((max_seq + k) / 2)


main()
