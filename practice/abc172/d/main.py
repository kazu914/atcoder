#!/usr/bin/env python3
import sys


def II(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


def LI(): return list(map(int, sys.stdin.readline().split()))


def g(i, N):
    tmp = N // i
    return int(i*tmp*(tmp+1)/2)


def main():
    N = II()
    ans = 0
    for i in range(1, N+1):
        ans += g(i, N)
    print(ans)


    # oj t -c "pypy3 main.py"
    # acc s main.py -- --guess-python-interpreter pypy
main()
