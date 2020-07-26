#!/usr/bin/env python3
import math
import sys


def II():
    return int(sys.stdin.readline())


def MI():
    return map(int, sys.stdin.readline().split())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def main():
    N, K = MI()
    ans = 0
    for n in range(1, N + 1):
        k = math.ceil(math.log2(K / n))
        ans += (1 / N) * min((1 / 2) ** k, 1)

    print(ans)


main()
