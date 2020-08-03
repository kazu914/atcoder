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

    for i in range(-200, 200):
        for j in range(-200, 200):
            if i ** 5 - j ** 5 == N:
                print(i, j)
                return


main()
