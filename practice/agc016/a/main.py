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
    S = input()

    indexes = {}

    for i in range(len(S)):
        if S[i] not in indexes.keys():
            indexes[S[i]] = [i]
        else:
            indexes[S[i]].append(i)

    ans = 100

    for k, v in indexes.items():
        tmp_max = v[0]
        tmp_max = max(v[0], len(S) - v[-1] - 1)
        v.append(len(S))
        for i in range(len(v) - 1):
            tmp_max = max(tmp_max, v[i+1] - v[i] - 1)
        ans = min(ans, tmp_max)
    print(ans)


main()
