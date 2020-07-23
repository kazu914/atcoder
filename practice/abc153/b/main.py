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
    H, N = MI()
    A = LI()

    if sum(A) >= H:
        print("Yes")
    else:
        print("No")


main()
