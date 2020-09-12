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

    mods = [0] * 2019

    ttl = 0
    pows = 1

    for i in range(len(S)-1, -1, -1):
        ttl += (int(S[i]) * pows) % 2019
        ttl %= 2019
        pows *= 10
        pows %= 2019
        mods[ttl] += 1

    mods[0] += 1
    ans = 0
    for i in range(2019):
        ans += mods[i] * (mods[i] - 1) / 2

    print(int(ans))


main()
