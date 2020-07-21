
import sys
from io import StringIO
import unittest


def resolve():
    a, r, n = map(int, input().split())

    ans = a * (r**(n-1))
    if ans > 10**9:
        print('large')
        return
    print(ans)


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
        input = """2 3 4"""
        output = """54"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 3 21"""
        output = """large"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """12 34 5"""
        output = """16036032"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
