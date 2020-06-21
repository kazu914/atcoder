import sys
from io import StringIO
import unittest


import collections


def resolve():
    n = int(input())
    targets = list(map(int, input().split()))
    q = int(input())
    ans = sum(targets)

    targets = collections.Counter(targets)

    for i in range(q):

        b, c = map(int, input().split())
        num_of_b = targets[b]
        targets.update({c: num_of_b})
        del targets[b]
        ans += (c-b)*num_of_b
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
        input = """4
1 2 3 4
3
1 2
3 4
2 4"""
        output = """11
12
16"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
1 1 1 1
3
1 2
2 1
3 5"""
        output = """8
4
4"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """2
1 2
3
1 100
2 100
100 1000"""
        output = """102
200
2000"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
