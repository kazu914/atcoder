import sys
from io import StringIO
import unittest

def resolve():
    N = int(input())

    A = [0 for i in range(N+1)]
    B = [0 for i in range(N+1)]
    C = [0 for i in range(N+1)]

    for i in range(1,len(A)):
        a,b,c = map(int,input().split())

        A[i] = max(B[i-1],C[i-1]) + a
        B[i] = max(C[i-1],A[i-1]) + b
        C[i] = max(A[i-1],B[i-1]) + c

    print(max(A[-1],B[-1],C[-1]))


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
10 40 70
20 50 80
30 60 90"""
        output = """210"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """1
100 10 1"""
        output = """100"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """7
6 7 8
8 8 3
2 5 2
7 8 6
4 6 8
2 3 4
7 5 1"""
        output = """46"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()