#!/usr/bin/env python3
import sys


def II(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


def LI(): return list(map(int, sys.stdin.readline().split()))


def main():
    N = LI()
    print(N[0]*N[1])


# oj t -c "pypy3 main.py"
# acc s main.py -- --guess-python-interpreter pypy
main()
