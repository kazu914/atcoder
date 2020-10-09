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
    H, W, K = MI()
    cake = []

    result = [[0 for w in range(W)] for h in range(H)]
    flag = 1

    for i in range(H):
        row = input()
        tmp = []
        for j in range(W):
            tmp.append(0 if row[j] == "." else 1)

        sum_tmp = sum(tmp)

        if sum_tmp == 0:
            if i > 0 and sum(result[i-1]) > 0:
                for j in range(W):
                    result[i][j] = result[i-1][j]
        elif sum_tmp == 1:
            for j in range(W):
                result[i][j] = flag
            flag += 1

        else:
            for j in range(W):
                result[i][j] = flag
                if tmp[j] == 1:
                    flag += 1
            if tmp[j] == 0:
                idx = -1
                while tmp[idx] == 0:
                    result[i][idx] = flag - 1
                    idx -= 1

        cake.append(tmp)

    for i in range(H):
        if sum(result[H - i - 1]) == 0:
            for j in range(W):
                result[H - i - 1][j] = result[H - i][j]

    for i in range(H):
        print(*result[i], sep=" ")


main()
