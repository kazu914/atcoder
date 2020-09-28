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
    a, b, c, d = MI()
    if a > c:
        a, b, c, d = c, d, a, b
    if c <= b:
        print("Yes")
        return
    print("No")


main()
