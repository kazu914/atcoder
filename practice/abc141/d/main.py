#!/usr/bin/env python3
import sys
import heapq


def II():
    return int(sys.stdin.readline())


def MI():
    return map(int, sys.stdin.readline().split())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def main():
    n, m = MI()
    a = LI()
    heap = []
    for i in range(n):
        heapq.heappush(heap, a[i] * -1)

    while m > 0:
        min_ = heapq.heappop(heap) * -1
        min_ = (min_ // 2) * -1
        heapq.heappush(heap, min_)
        m -= 1
    print(sum(heap) * -1)


main()
