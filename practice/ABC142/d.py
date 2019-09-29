import sys
from io import StringIO
import unittest


def divisor(n):
    i = 1
    table = []

    while i * i <= n:
        if n % i == 0:
            table.append(i)
            table.append(n // i)
        i += 1
    table = list(set(table))

    return table


def common_divisor(a, b):
    table = []
    for i in a:
        if i in b:
            table.append(i)
    return table


def resolve():
    A, B = map(int, input().split())
    a_list = divisor(A)
    b_list = divisor(B)
    common_list = common_divisor(a_list, b_list) if len(a_list) < len(b_list) else common_divisor(b_list, a_list)
    common_list.sort()

    i = 1
    while i < len(common_list):
        j = i + 1
        while j < len(common_list):
            if common_list[j] % common_list[i] == 0:
                del common_list[j]
            else:
                j += 1
        i += 1

    print(len(common_list))


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
        input = """12 18"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """420 660"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """1 2019"""
        output = """1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
