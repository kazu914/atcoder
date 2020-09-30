#!/usr/bin/env python3
import collections as cl
import sys


def II():
    return int(sys.stdin.readline())


def MI():
    return map(int, sys.stdin.readline().split())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def main():
    S = input()
    T = input()

    s_dict = {}
    t_dict = {}

    s_count = 0
    t_count = 0

    for i in range(len(S)):
        s = S[i]
        t = T[i]
        s_new = -1
        t_new = -1

        if s in s_dict.keys():
            s_new = str(s_dict[s])
        else:
            s_dict[s] = s_count
            s_new = str(s_count)
            s_count += 1

        if t in t_dict.keys():
            t_new = str(t_dict[t])
        else:
            t_dict[t] = t_count
            t_new = str(t_count)
            t_count += 1

        if s_new != t_new:
            print("No")
            return

    print("Yes")


main()
