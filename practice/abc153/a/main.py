#!/usr/bin/env python3
import collections as cl
import sys


def II():
    return int(sys.stdin.readline())


def MI():
    return map(int, input().split())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def main():
    h, a = MI()

    ans = h // a
    if h % a != 0:
        ans += 1
    print(ans)


main()
