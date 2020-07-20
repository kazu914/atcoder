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
    a, b, c = MI()

    n = set([a, b, c])
    print("Yes" if len(n) == 2 else "No")


main()
