#!/usr/bin/env python3
import sys
import collections as cl
import math

def II(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


def LI(): return list(map(int, sys.stdin.readline().split()))


def main():
    A,B = MI()
    for i in range(11000):
        if math.floor( i * 0.08 ) == A and math.floor(i * 0.1) == B:
            print(i)
            exit()

    print(-1)


main()
