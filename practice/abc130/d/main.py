#!/usr/bin/env python3
import sys
import collections as cl


def II():
    return int(sys.stdin.readline())


def MI():
    return map(int, sys.stdin.readline().split())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def main():
    n, k = MI()
    a = LI()
    r = 0
    ans = 0
    ttl = 0

    for left in range(n):
        while ttl < k and r < n:
            ttl += a[r]
            r += 1
        if ttl < k:
            break
        ans += n - r + 1
        ttl -= a[left]
    print(ans)


main()
