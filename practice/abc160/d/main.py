#!/usr/bin/env python3
import sys
import collections as cl


def II():
    return int(sys.stdin.readline())


def MI():
    return map(int, sys.stdin.readline().split())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def main():
    n, x, y = MI()
    ans = [0] * (n)

    for i in range(1, n + 1):
        for j in range(i + 1, n + 1):
            dis = min(j - i, abs(i - x) + abs(j - y) + 1)
            ans[dis] += 1

    for i in range(1, n):
        print(ans[i])


main()
