#!/usr/bin/env python3
import collections as cl
import sys


def II():
    return int(sys.stdin.readline())


def MI():
    return map(int, sys.stdin.readline().split())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def base_10_to_n(x, n):
    """
    xをn進数表記にする．
    ０埋めしたい場合は返り値に対して，
    result.zfill(5)
    のようにする
    """
    if (int(x//n)):
        return base_10_to_n(int(x/n), n) + str(x % n)
    return str(x % n)


def main():
    N, K = MI()
    targets = []

    for i in range(N):
        target = LI()
        targets.append(target)

    for i in range(K**N):
        i_str = base_10_to_n(i, K)
        i_str = i_str.zfill(N)
        res = 0
        for question_num in range(N):
            choice = int(i_str[question_num])
            res ^= targets[question_num][choice]
        if res == 0:
            print("Found")
            return
    print("Nothing")


main()
