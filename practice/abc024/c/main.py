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
    N, D, K = MI()
    ranges = []

    for i in range(D):
        tmp = LI()
        ranges.append(tmp)

    ans = []

    for i in range(K):
        s, t = MI()
        for k in range(D):
            l, r = ranges[k]
            if l <= s <= r:
                if l <= t <= r:
                    ans.append(k + 1)
                    break
                s = r if s < t else l

    print(*ans, sep="\n")


main()
