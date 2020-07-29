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
    s = input()
    answer = [0] * len(s)
    nearest_R = 0
    nearest_L = 0

    for i in range(len(s)):
        if s[i] == "R":
            nearest_R = i
        else:
            if (i - nearest_R) % 2 == 0:
                answer[nearest_R] += 1
            else:
                answer[nearest_R + 1] += 1

        li = len(s) - i - 1
        if s[li] == "L":
            nearest_L = li
        else:
            if (nearest_L - li) % 2 == 0:
                answer[nearest_L] += 1
            else:
                answer[nearest_L - 1] += 1
    print(*answer, sep=" ")


main()
