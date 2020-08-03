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
    _ = II()
    a = LI()

    ans = []
    all_xor = 0
    for _a in a:
        all_xor ^= _a

    for _a in a:
        ans.append(all_xor ^ _a)
    print(*ans, sep=" ")


main()
