#!/usr/bin/env python3
import collections as cl
import sys


def II():
    return int(sys.stdin.readline())


def MI():
    return map(int, sys.stdin.readline().split())


def LI():
    return list(map(int, sys.stdin.readline().split()))


MAX = 10 ** 5 + 1


def main():
    Q = II()
    queries = []
    for i in range(Q):
        query = LI()
        queries.append(query)

    era = [0] * MAX

    for i in range(2, MAX):
        origin = i
        while origin < MAX:
            if era[origin] >= 2:
                break
            era[origin] += 1
            origin += i

    ruiseki = [0] * MAX

    for i in range(1, MAX):
        ruiseki[i] = ruiseki[i-1]
        if era[i] == era[int((i + 1) / 2)] == 1:
            ruiseki[i] += 1

    for query in queries:
        r, l = query

        print(ruiseki[l] - ruiseki[r-1])


main()
