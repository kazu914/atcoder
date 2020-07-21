import sys
from io import StringIO
import unittest


def resolve():
    n = int(input())

    nums = []
    for i in range(n):
        nums.append(int(input()))
    flag = [0 for i in range(n)]
    nums.sort()
    if(len(set(nums)) == len(nums)):
        print('Correct')
        return

    for i in nums:
        flag[i-1] += 1

    x = flag.index(2) + 1
    y = flag.index(0) + 1

    print(x, y)


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
        input = """6
1
5
6
3
2
6"""
        output = """6 4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """7
5
4
3
2
7
6
1"""
        output = """Correct"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
