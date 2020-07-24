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
    _a, _b = input().split()

    a = _a * int(_b)
    b = _b * int(_a)
    print(a if a < b else b)


main()
