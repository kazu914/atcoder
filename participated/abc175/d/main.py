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
    n, k = MI()
    p = LI()
    c = LI()

    hairetu = [[0] for i in range(n)]
    for i in range(n):
        next_idx = i + 1
        hairetu[i][0] = c[i]
        for times in range(1, n):
            next_idx = p[next_idx - 1]
            hairetu[i].append(hairetu[i][times - 1] + c[next_idx - 1])
            if next_idx == i + 1:
                break

    max_candidate = [-1 * 10 ** 18] * n
    for i in range(n):
        q = k // len(hairetu[i])
        r = k % len(hairetu[i])

        if q == 0:
            max_candidate[i] = max(*hairetu[i][:k])

        loop = hairetu[i][-1]
        if loop <= 0:
            max_candidate[i] = max(*hairetu[i])

        else:
            tmp = [0] * len(hairetu[i])
            for j in range(len(hairetu[i])):
                if j <= r:
                    tmp[j] = q * loop + hairetu[i][j]

                else:
                    tmp[j] = (q-1)*loop + hairetu[i][j]
            max_candidate[i] = max(*tmp)

    print(max(*max_candidate))


main()
