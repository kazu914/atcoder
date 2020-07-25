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
    scores = LI()

    for i in range(k, n):
        next_score = scores[i] / scores[i - k]
        print("Yes" if next_score > 1 else "No")


main()
