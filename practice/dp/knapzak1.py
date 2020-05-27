import sys
from io import StringIO
import unittest


def resolve():
    N,W = map(int,input().split())
    weights = [0]
    values  = [0]
    for i in range(N):
        w,v = map(int,input().split())
        weights.append(w)
        values.append(v)

    min_costs = [[0 for i in range(W+1)] for i in range(N+1)]

    for ni in range(1,len(min_costs)):
        for wi in range(1,len(min_costs[ni])):
            if wi < weights[ni]:
                min_costs[ni][wi] = min_costs[ni -1][wi]
            else:
                min_costs[ni][wi] = max(min_costs[ni -1][wi],min_costs[ni -1][wi-weights[ni]] + values[ni])

    print(min_costs[-1][-1])

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
        input = """3 8
3 30
4 50
5 60"""
        output = """90"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """5 5
1 1000000000
1 1000000000
1 1000000000
1 1000000000
1 1000000000"""
        output = """5000000000"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """6 15
6 5
5 6
6 4
6 6
3 5
7 2"""
        output = """17"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()