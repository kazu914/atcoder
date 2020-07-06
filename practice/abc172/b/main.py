#!/usr/bin/env python3
import sys


def II(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


def LI(): return list(map(int, sys.stdin.readline().split()))


def main():
    a = input()
    b = input()
    ans = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            ans += 1
    print(ans)


# oj t -c "pypy3 main.py"
# acc s main.py -- --guess-python-interpreter pypy
main()
