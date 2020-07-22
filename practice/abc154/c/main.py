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
    S = LI()

    if len(set(S)) == N:
        print("YES")
    else:
        print("NO")


main()
