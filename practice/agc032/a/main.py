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
    A = LI()
    ans = []

    while len(A) > 0:
        idx = -1
        for i in range(len(A)):
            if i + 1 == A[i]:
                idx = i

        if idx == -1:
            print(-1)
            return

        A.remove(idx+1)

        ans.append(idx + 1)
    ans.reverse()

    for a in ans:
        print(a)


main()
