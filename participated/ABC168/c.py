import sys
from io import StringIO
import unittest


import math
import numpy


def resolve():
    a, b, h, m = map(int, input().split())

    ar = 30 * (h) + 30 * (m / 60)
    br = 6 * (m)

    ay = math.sin(math.radians(-ar + 90)) * a
    ax = math.cos(math.radians(-ar+90)) * a

    by = math.sin(math.radians(-br+90)) * b
    bx = math.cos(math.radians(-br+90)) * b

    av = numpy.array([ax, ay])
    bv = numpy.array([bx, by])

    u = bv-av

    print(numpy.linalg.norm(u))


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
        input = """3 4 9 0"""
        output = """5.00000000000000000000"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 4 10 40"""
        output = """4.56425719433005567605"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
