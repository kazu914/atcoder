import sys
from io import StringIO
import unittest

import math


def resolve():
    x = int(input())
    c = 100
    i = 0
    while c < x:
        i += 1
        c = math.floor(c * 1.01)
    print(i)


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
        input = """103"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1000000000000000000"""
        output = """3760"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1333333333"""
        output = """1706"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
