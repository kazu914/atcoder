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
    S = input()
    T = input()

    ans = 10000

    for i in range(len(S) - len(T) + 1):
        sub = 0
        for j in range(len(T)):
            if S[i + j] != T[j]:
                sub += 1

        ans = min(ans, sub)

    print(ans)


main()
