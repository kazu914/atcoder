

import sys
from io import StringIO
import unittest


def resolve():
    n, k = map(int, input().split())
    flag = [1 for i in range(n)]
    for i in range(k):
        d = int(input())
        Sunukes = list(map(int, input().split()))
        for sunuke in Sunukes:
            flag[sunuke-1] = 0
    print(sum(flag))


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
        input = """3 2
2
1 3
1
3"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """3 3
1
3
1
3
1
3"""
        output = """2"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
