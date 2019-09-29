import sys
from io import StringIO
import unittest


def devide(target, step):
    if (target % 2 == 0):
        step += 1
        step = devide(target / 2, step)

    return step


def resolve():
    N = int(input())
    targets = list(map(int, input().split()))
    min_step = 10000
    for i in range(N):
        step = devide(targets[i], 0)
        if(step < min_step):
            min_step = step
    print(min_step)


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
        input = """3
8 12 40"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
5 6 8 10"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """6
382253568 723152896 37802240 379425024 404894720 471526144"""
        output = """8"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
