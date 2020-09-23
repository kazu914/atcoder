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
    targets = []
    for i in range(N):
        a = II()
        targets.append([a, i])

    targets.sort()

    prev = targets[0][0]
    targets[0][0] = 0
    ans = [0] * N

    for i in range(1, N):
        if targets[i][0] == prev:
            targets[i][0] = targets[i-1][0]
        else:
            prev = targets[i][0]
            targets[i][0] = targets[i-1][0] + 1

        ans[targets[i][1]] = targets[i][0]

    print(*ans, sep="\n")


main()
