# 書きかけ

import sys
from io import StringIO
import unittest


def resolve():
    N, K = [int(x) for x in input().split()]
    hopes = []
    for i in range(N):
        x, y, c = input().split()
        if c == "W":
            y = int(y) + K
            c = "B"
        x = int(x) % (2 * K)
        y = int(y) % (2 * K)

        hopes.append([int(x), int(y), c])

    print(hopes)


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
        input = """4 3
0 1 W
1 2 W
5 3 B
5 4 B"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2 1000
0 0 B
0 1 W"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6 2
1 2 B
2 1 W
2 2 B
1 0 B
0 6 W
4 5 W"""
        output = """4"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
