#!/usr/bin/env python3
import sys


def II():
    return int(sys.stdin.readline())


def main():
    N = II()
    targets = []

    longest = 0
    sum_length = 0
    for i in range(N):
        d = II()
        longest = max(d, longest)
        sum_length += d
    print(sum_length)
    rest = sum_length - longest
    min_length = 0 if rest >= longest else longest - rest

    print(min_length)


main()
