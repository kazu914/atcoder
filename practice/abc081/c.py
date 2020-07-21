import sys
from io import StringIO
import unittest


def resolve():
    N, K = map(int, input().split())
    targets = list(map(str, input().split()))
    targets_dict = {}

    for i in range(N):
        if targets[i] not in targets_dict:
            targets_dict[targets[i]] = 1
        else:
            targets_dict[targets[i]] += 1

    need_reduce = len(targets_dict) - K

    if need_reduce <= 0:
        print(0)
    else:
        ans = 0
        targets_dict = sorted(targets_dict.items(), key=lambda x: x[1])
        for i in range(need_reduce):
            ans += targets_dict[i][1]
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
        input = """5 2
1 1 2 2 5"""
        output = """1"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 4
1 1 2 2"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 3
5 1 3 2 4 1 1 2 3 4"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
