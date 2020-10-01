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
    S = input()

    W_num = 0
    E_num = 0

    for i in range(N):
        if S[i] == "W":
            W_num += 1
        else:
            E_num += 1

    left_E = 0
    left_W = 0

    ans = N

    for i in range(N):
        right_E = E_num - left_E
        if S[i] == "E":
            right_E -= 1
            left_E += 1

        ans = min(ans, right_E + left_W)
        if S[i] == "W":
            left_W += 1

    print(ans)


main()
