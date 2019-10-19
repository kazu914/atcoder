import sys
from io import StringIO
import unittest
import bisect


def check(a, b, c):
    return True if c < a + b else False

def resolve():
    n = int(input())
    targets = list(map(int, input().split()))
    targets.sort()
    ans = 0

    for i in range(len(targets)):
        for j in range(i + 1, len(targets)):
            for k in range(j + 1, len(targets)):
                if check(targets[i], targets[j], targets[k]):
                    ans += 1
                else:
                    continue

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
3 4 2 1"""
        output = """1"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """3
1 1000 1"""
        output = """0"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """7
218 786 704 233 645 728 389"""
        output = """23"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()