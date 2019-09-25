import sys
from io import StringIO
import unittest

def resolve():
    N = int(input())
    targets = []
    for i in range(N):

        targets.append([int(x) for x in input().split()])

    now = [0,0]
    now_t = 0

    for target in targets:
        distance = abs(now[0] - target[1]) + abs(now[1] - target[2])
        limit = target[0] - now_t
        if distance > limit :
            print("No")
            exit()
        elif distance - limit %2 !=0:
            print("No")
            exit()
        else:
            now[0] = target[1]
            now[1] = target[2]
            now_t  = target[0]
    print("Yes")

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
3 1 2
6 1 1"""
        output = """Yes"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """1
2 100 100"""
        output = """No"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """2
5 1 1
100 1 1"""
        output = """No"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()