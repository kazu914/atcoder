#!/usr/bin/env python3
import sys
import collections as cl


def II(): return int(sys.stdin.readline())


def MI(): return map(int, sys.stdin.readline().split())


def LI(): return list(map(int, sys.stdin.readline().split()))


def main():
    N = II()
    X = input()
    f_memo = [-1] * len(X)**2
    f_memo[0] = 0

    next_pop = [-1] * len(X)**2

    for i in range(1, N+1):
        if X[i-1] == '0':
            reversed_X = X[:i-1]+'1' + X[i:]
        else:
            reversed_X = X[:i-1]+'0' + X[i:]
        count = -1
        n = reversed_X
        while n != '0':
            counter = cl.Counter(n)
            count += 1
            num_1 = counter['1']
            if num_1 ==0:
                break
            n = bin(int(n, 2) % num_1)

        print(count)


        # oj t -c "pypy3 main.py"
        # acc s main.py -- --guess-python-interpreter pypy
main()
