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
    N = II()
    yama = LI()
    sum_ame = sum(yama)
    sum_kisuu = 0
    for i in range(1, N, 2):
        sum_kisuu += yama[i]

    ans = [0] * N
    ans[0] = sum_ame - 2 * sum_kisuu

    for i in range(1, N):
        ans[i] = 2 * yama[i - 1] - ans[i - 1]

    print(*ans, sep=" ")


main()
