import sys
from io import StringIO
import unittest


def resolve():
    n = int(input())
    str_list = [[] for i in range(n)]
    for i in range(n):
        rows = input()
        for item in rows:
            str_list[i].append(item)
    ans = ''
    for i in range(n):
        common = set(str_list[i]) & set(str_list[n - 1-i])
        if len(common) == 0:
            print(-1)
            return
        else:
            ans += list(common)[0]
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
        input = """2
yc
ys"""
        output = """yy"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """2
rv
jh"""
        output = """-1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
