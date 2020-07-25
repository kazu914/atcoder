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
    N = II()

    kyu = 9

    N -= 400

    while N >= 0:
        N -= 200
        kyu -= 1

    print(kyu)


main()
