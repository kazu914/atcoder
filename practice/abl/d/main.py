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
    A = []
    max_a = 0
    for i in range(N):
        a = II()
        A.append(a)
        max_a = max(max_a, a)

    dp = [0] * N
    last_index = [-1] * (max_a + 1)

    for i in range(N):
        pres = []
        target = A[i]
        for k in range(target-K, target+K+1):
            if k < 0 or k > max_a:
                continue
            if last_index[k] == -1:
                pres.append(1)
                continue
            pres.append(dp[last_index[k]] + 1)
        dp[i] = max(pres)
        last_index[target] = i

    print(max(dp))


main()
