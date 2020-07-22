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
    s, t = input().split()
    a, b = MI()
    u = input()

    if s == u:
        a -= 1
    else:
        b -= 1
    print(a, b)


main()
