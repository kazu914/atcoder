#!/usr/bin/env python3
import sys
import collections as cl


def II(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


def LI(): return list(map(int, sys.stdin.readline().split()))


def main():
    N = II()
    num = 0
    for i in range(N):
        a, b = MI()
        if a == b:
            num += 1
            if num == 3:
                print("Yes")
                return
        else:
            num = 0

    print("No")


main()
