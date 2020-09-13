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
    N = input()
    targets = LI()
    for i in range(len(targets)):
        target = targets[i]
        while target % 2 == 0:
            target /= 2
        targets[i] = target

    print(len(set(targets)))


main()
