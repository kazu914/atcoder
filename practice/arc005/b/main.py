#!/usr/bin/env python3
import sys


def II():
    return int(sys.stdin.readline())


def MI():
    return map(int, sys.stdin.readline().split())


def LI():
    return list(map(int, sys.stdin.readline().split()))


def define_way(W):
    if W == "R":
        return [0, 1]
    if W == "L":
        return [0, -1]
    if W == "U":
        return [-1, 0]
    if W == "D":
        return [1, 0]
    if W == "RU":
        return [-1, 1]
    if W == "RD":
        return [1, 1]
    if W == "LU":
        return [-1, -1]
    if W == "LD":
        return [1, -1]


class Solver():
    def __init__(self, passwords, way, start_position):
        self.passwords = passwords
        self.way = way
        self.start_position = start_position

    def solve(self):
        x = self.start_position[0]
        y = self.start_position[1]
        ans = ''

        for i in range(4):
            ans += str(self.passwords[x][y])
            if x == 0 and self.way[0] == -1:
                self.way[0] = 1
            if x == 8 and self.way[0] == 1:
                self.way[0] = -1
            if y == 0 and self.way[1] == -1:
                self.way[1] = 1
            if y == 8 and self.way[1] == 1:
                self.way[1] = -1
            x += self.way[0]
            y += self.way[1]

        print(ans)


def main():
    x, y, W = input().split()
    x = int(x)
    y = int(y)

    passwords = []
    for i in range(9):
        row = input()
        tmp = []
        for j in range(9):
            tmp.append(str(row)[j])
        passwords.append(tmp)

    way = define_way(W)

    solver = Solver(passwords, way, (y - 1, x-1))
    solver.solve()


main()
