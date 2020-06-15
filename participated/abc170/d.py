import sys
from io import StringIO
import unittest


def resolve():
    _ = int(input())
    targets = list(map(int, input().split()))

    targets.sort()
    dup = [0 for i in range(10**6+1)]

    for target in targets:
        target_m = target
        while target_m <= 10**6:
            dup[target_m - 1] += 1
            if dup[target_m - 1] >= 2:
                break
            target_m += target

    ans = 0
    targets = set(targets)
    for i in range(len(dup)):
        if (dup[i] == 1) and i+1 in targets:
            ans += 1

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
        input = """5
24 11 8 3 16"""
        output = """3"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
5 5 5 5"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10
33 18 45 28 8 19 89 86 2 4"""
        output = """5"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
