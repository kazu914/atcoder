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
    N, K = MI()

    bunbo = N ** 3
    bunshi = 0
    bunshi += (K - 1) * (N - K) * 6
    bunshi += (N - K) * 3
    bunshi += (K - 1) * 3
    bunshi += 1

    print((bunshi / bunbo))


main()
