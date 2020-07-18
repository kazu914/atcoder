#!/usr/bin/env python3
import sys
import collections as cl


def II(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


def LI(): return list(map(int, sys.stdin.readline().split()))


def main():
    N,A,B = MI()
    oneset = A + B

    rep = N // oneset

    print(rep * A + min(N % oneset,A))


main()
