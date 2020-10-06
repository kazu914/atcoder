#!/usr/bin/env python3
import sys


def II():
    return int(sys.stdin.readline())


def MI():
    return map(int, sys.stdin.readline().split())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def main():
    N = II()
    ans = []

    for i in range(N):
        a = II()

        flag = True
        k = 0
        while flag and k < len(ans):
            if ans[k] >= a:
                ans[k] = a
                flag = False
            k += 1

        if flag:
            ans.append(a)

    print(len(ans))


main()
