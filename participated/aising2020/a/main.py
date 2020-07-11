#!/usr/bin/env python3
import sys


def II(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


def LI(): return list(map(int, sys.stdin.readline().split()))


def main():
    L, R, d = MI()
    ans = 0
    for i in range(L,R+1):
        if i % d == 0:
            ans+=1
    print(ans)
            


# oj t -c "pypy3 main.py"
# acc s main.py -- --guess-python-interpreter pypy
main()
