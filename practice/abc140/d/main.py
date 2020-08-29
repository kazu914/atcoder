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
    original = input()
    num_happy = 0

    for i in range(N - 1):
        if original[i] == original[i+1]:
            num_happy += 1

    print(min(N-1, num_happy + 2 * K))


main()
