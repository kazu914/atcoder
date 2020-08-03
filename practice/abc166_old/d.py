import sys
from io import StringIO
import unittest


def resolve():
    x = int(input())
    a, b = -round(x**(1/5)), -round(x**(1/5))
    while a ** 5 < x:
        b = -round(x**(1/5))
        while b ** 5 < x:
            if (a ** 5 + b ** 5 == x):
                print(a, b)
                return
            b += 1
        a += 1


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
        input = """33"""
        output = """2 -1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """1"""
        output = """0 -1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
