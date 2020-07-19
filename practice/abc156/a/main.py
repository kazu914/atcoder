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
    N, R = MI()
    if N >= 10:
        print(R)
    else:
        print(R + 100 * (10 - N))


main()
