import sys
from io import StringIO
import unittest


def resolve():
    n = int(input())
    q = int(input())


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
        input = """2
19
4 1 1
4 1 2
4 2 1
4 2 2
3
4 1 1
4 1 2
4 2 1
4 2 2
1 1 2
4 1 1
4 1 2
4 2 1
4 2 2
2 2 1
4 1 1
4 1 2
4 2 1
4 2 2"""
        output = """0
1
2
3
0
2
1
3
1
3
0
2
3
1
2
0"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3
9
2 2 3
3
1 2 1
2 3 2
1 1 3
3
4 1 1
4 2 2
4 2 3"""
        output = """1
6
8"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
