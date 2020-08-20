#!/usr/bin/env python3
import collections as cl
import sys


def II():
    return int(sys.stdin.readline())


def main():
    n = II()
    if n % 2 == 1:
        print(0)
        return

    n_int = n // 2
    ans_int = 0

    k = 5
    while k <= n_int:
        ans_int += n_int//k
        k *= 5

    print(ans_int)


main()
