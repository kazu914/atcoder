#!/usr/bin/env python3
import collections as cl
import sys


def II():
    return int(sys.stdin.readline())


def MI():
    return map(int, sys.stdin.readline().split())


def LI():
    return list(map(int, sys.stdin.readline().split()))


A = "dream"
B = "dreamer"
C = "erase"
D = "eraser"


def main():
    S = input()
    T = []
    i = 0
    while i <= len(S)-1:
        target = S[i:i+5]
        if target == A:
            i += len(A)
            T.append("A")
            continue
        if target == C:
            i += len(C)
            T.append("C")
            continue
        T.append(target[0])
        i += 1

    if T[0] != "A" and T[0] != "C":
        print("NO")
        return

    for i in range(1, len(T)):
        if T[i] == 'r':
            if T[i-1] == "e":
                if i >= 2 and T[i-2] == "A":
                    continue
                print('NO')
                return
            if T[i-1] == "C":
                continue
            print('NO')
            return

    print('YES')


main()
