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
    n = input()
    ans = 0
    for i in range(len(n)):
        ans += int(n[i])

    if ans % 9 == 0:
        print("Yes")
    else:
        print("No")


main()
