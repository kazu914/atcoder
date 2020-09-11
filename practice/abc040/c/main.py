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
    N = II()
    hashias = LI()
    dp = [0] * (N)
    dp[1] = abs(hashias[1] - hashias[0]
                )
    for i in range(2, N):
        dp[i] = min(dp[i-2] + abs(hashias[i-2] - hashias[i]),
                    dp[i-1] + abs(hashias[i-1] - hashias[i]))
    print(dp[-1])


main()
