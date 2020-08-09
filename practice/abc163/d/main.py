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
    n, k = MI()
    ans = 0
    ttl = n * (n + 1) / 2

    for i in range(k, n + 2):
        min_i = i * (i - 1) / 2
        max_i = ttl - (n - i) * (n - i + 1) / 2
        ans += (max_i - min_i + 1) % (10 ** 9 + 7)
        ans %= 10 ** 9 + 7

    print(int(ans))


main()
