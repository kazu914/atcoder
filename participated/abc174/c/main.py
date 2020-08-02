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
    k = II()

    amari = 0
    for i in range(k):
        amari = (amari * 10 + 7) % k
        if amari == 0:
            print(i + 1)
            return
    print(-1)


main()
