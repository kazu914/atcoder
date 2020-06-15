import sys
from io import StringIO
import unittest


from collections import deque


class Maze:
    def __init__(self, hardles, x, y):
        self.hardles = hardles
        self.costs = [[10**9 for i in range(401)] for j in range(401)]
        self.costs[200][200] = 0
        self.calcCosts(x, y)

    def calcCosts(self, target_x, target_y):
        stack = deque()
        stack.append([200, 200])
        while len(stack) > 0:
            sunuke = stack.popleft()
            self.calcNeighbar(stack, sunuke[0], sunuke[1])
        print(self.costs[target_x][target_y])

    def calcNeighbar(self, stack, x, y):
        ways = [[-1, 0], [-1, 1], [0, -1], [0, 1], [1, 0], [1, 1]]
        for way in ways:
            neibhbar_x = x + way[0]
            neibhbar_y = y + way[1]
            if(0 <= neibhbar_x <= 400 and 0 <= neibhbar_y <= 400):

                if (self.hardles[neibhbar_x][neibhbar_y] == 0) and (
                        self.costs[neibhbar_x][neibhbar_y] > self.costs[x][y] + 1):

                    self.costs[neibhbar_x][neibhbar_y] = self.costs[x][y] + 1
                    stack.append([neibhbar_x, neibhbar_y])


def resolve():
    n, x, y = map(int, input().split())
    x += 200
    y += 200
    hardles = [[0 for i in range(401)] for j in range(401)]
    for i in range(n):
        _x, _y = map(int, input().split())
        hardles[_x+200][_y+200] = 1
    maze = Maze(hardles, x, y)


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """1 2 2
1 1"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1 2 2
2 1"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5 -2 3
1 1
-1 1
0 1
-2 1
-3 1"""
        output = """6"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
