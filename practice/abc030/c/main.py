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
    N, M = MI()
    X, Y = MI()
    A = LI()
    B = LI()

    ans = 0
    side = 0
    time = 0
    x_idx = 0
    y_idx = 0

    while x_idx < N and y_idx < M:
        if side == 0:
            while A[x_idx] < time:
                x_idx += 1
                if x_idx >= N:
                    print(ans)
                    return
            time = A[x_idx] + X
            side = 1

        if side == 1:
            while B[y_idx] < time:
                y_idx += 1
                if y_idx >= M:
                    print(ans)
                    return
            time = B[y_idx] + Y
            side = 0
            ans += 1

    print(ans)


main()
