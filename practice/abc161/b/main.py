#!/usr/bin/env python3
import sys
import collections as cl


def II(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


def LI(): return list(map(int, sys.stdin.readline().split()))


def main():
    N, M = MI()
    A = LI()

    shre = sum(A) / (4 * M)
    ans = 0
    for a in A:
        if a >= shre:
            ans += 1
    print("Yes" if ans >= M else "No")


main()
