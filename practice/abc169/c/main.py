#!/usr/bin/env python3
import sys
import math as Math


def II(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


def LI(): return list(map(int, sys.stdin.readline().split()))


def main():
    a, b = input().split()
    a = int(a)
    b = int(b.replace(".", ""))
    print(int(a*b//100))


# oj t -c "pypy3 main.py"
# acc s main.py -- --guess-python-interpreter pypy
main()
