import sys
from io import StringIO
import unittest


def resolve():
    n = int(input())

    ans = []
    while n > 0:
        n, mod = divmod(n, 26)
        if mod == 0:
            ans.append(26)
            n -= 1
        else:
            ans.append(mod)

    ans.reverse()

    for i in range(len(ans)):
        if ans[i] == 0:
            pass
        else:
            print(chr(96+ans[i]), end='')
    print()


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
        input = """2"""
        output = """b"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """27"""
        output = """aa"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """123456789"""
        output = """jjddja"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
