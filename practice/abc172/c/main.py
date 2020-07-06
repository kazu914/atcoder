#!/usr/bin/env python3
import sys
from collections import deque


def II(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


def LI(): return list(map(int, sys.stdin.readline().split()))


def main():
    n, m, k = MI()
    a = deque(LI())
    b = deque(LI())

    ans = 0
    canContinue = True
    while canContinue:
        if len(a) == 0 and len(b) == 0:
            canContinue = False
            break
        if len(b) == 0:
            a_top = a.pop()
            k -= a_top
            if (k < 0):
                canContinue = False
                break
            ans += 1
            continue

        if len(a) == 0:
            b_top = b.pop()
            k -= b_top
            if (k < 0):
                canContinue = False
                break
            ans += 1
            continue

        a_top = a[0]
        b_top = b[0]

        if a_top <= b_top:
            a_top = a.pop()
            k -= a_top
            if (k < 0):
                canContinue = False
                break
            ans += 1
            continue
        else:
            b_top = b.pop()
            k -= b_top
            if (k < 0):
                canContinue = False
                break
            ans += 1
            continue
    print(ans)


# oj t -c "pypy3 main.py"
# acc s main.py -- --guess-python-interpreter pypy
main()
