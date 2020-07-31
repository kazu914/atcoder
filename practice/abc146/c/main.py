#!/usr/bin/env python3
import collections as cl
import math
import sys


def II():
    return int(sys.stdin.readline())


def MI():
    return map(int, sys.stdin.readline().split())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def binary_search(left, right, a, b, x):
    if left + 1 == right or left == right:
        return left
    center = math.floor((left + right) / 2)

    keta = len(str(center))

    result = center * a + keta * b

    if result > x:
        return binary_search(left, center, a, b, x)

    else:
        return binary_search(center, right, a, b, x)


def main():
    a, b, x = MI()

    ans = binary_search(0, math.ceil(x // a), a, b, x)

    print(min(ans, 10 ** 9))


main()
