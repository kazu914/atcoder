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
    K, T = MI()
    types = LI()

    types.sort(reverse=True)
    max_num = types[0]
    others_num = sum(types[1:])
    ans = max(max_num - 1 - others_num, 0)
    print(ans)


main()
