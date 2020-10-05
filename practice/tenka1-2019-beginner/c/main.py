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
    targets = []
    ruiseki = [0] * N

    ttl_0 = 0

    for i in range(N):
        targets.append(0 if S[i] == "." else 1)
        if S[i] == ".":
            ttl_0 += 1

    ruiseki[0] = targets[0]
    for i in range(1, N):
        ruiseki[i] = ruiseki[i-1] + targets[i]

    ans = N

    for k in range(N+1):
        left_1 = ruiseki[k-1] if k > 0 else 0
        right_0 = ttl_0 - (k - left_1)
        ans = min(ans, left_1 + right_0)

    print(ans)


main()
