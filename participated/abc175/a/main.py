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

    ans = 0

    if S[0] == S[1] == S[2] == "R":
        print(3)
        return

    if S[0] == S[1] == S[2] == "S":
        print(0)
        return

    for i in range(1, 3):
        if S[i-1] == S[i] == 'R':
            ans += 1

    print(ans + 1)


main()
