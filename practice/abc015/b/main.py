#!/usr/bin/env python3
import collections as cl
import sys
import math


def II():
    return int(sys.stdin.readline())


def MI():
    return map(int, sys.stdin.readline().split())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def main():
    N = II()
    softwares = LI()

    ttl = 0
    num = 0

    for bug in softwares:
        if bug == 0:
            continue
        ttl += bug
        num += 1

    print(math.ceil(ttl / num))


main()
