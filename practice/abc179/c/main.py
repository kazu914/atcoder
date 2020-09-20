#!/usr/bin/env python3
import sys
import collections as cl


def II(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


def LI(): return list(map(int, sys.stdin.readline().split()))


def main():
    N = II()

    ans = 1
    for a in range(1, N-1):
        num_b = (N-1) // a
        ans += num_b

    print(ans)


main()
