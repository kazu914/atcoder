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
    X = LI()

    ans = 10 ** 9

    for i in range(1, 101):
        sum_temp = 0
        for x in X:
            sum_temp += (x - i) ** 2

        if sum_temp <= ans:
            ans = sum_temp
    print(ans)


main()
