#!/usr/bin/env python3
import sys
import collections as cl


def II(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


def LI(): return list(map(int, sys.stdin.readline().split()))


def main():
    K, N = MI()
    A = LI()

    dis = [0] * len(A)
    dis[0] = A[0] + (K - A[-1])
    for i in range(1, N):
        dis[i] = A[i] - A[i - 1]

    max_dis = max(dis)

    print(K-max_dis)


main()
