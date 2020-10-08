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
    S = input()
    count_left = 0
    to_be_add_left = 0

    for s in S:
        if s == "(":
            count_left += 1
        else:
            if count_left == 0:
                to_be_add_left += 1
            else:
                count_left -= 1

    count_right = 0
    to_be_add_right = 0

    for i in range(len(S)):
        if S[N - i - 1] == ")":
            count_right += 1
        else:
            if count_right == 0:
                to_be_add_right += 1
            else:
                count_right -= 1

    left = ["("] * to_be_add_left
    right = [")"] * to_be_add_right
    print("".join([*left, S, *right]))


main()
