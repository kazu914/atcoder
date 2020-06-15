import sys
from io import StringIO
import unittest

def resolve():
    MAX_COST = 10**9
    num_steps = int(input())

    steps = list(map(int,input().split()))

    min_cost = [MAX_COST for i in range(num_steps)]
    min_cost[0] = 0
    min_cost[1] = abs(steps[1] - steps[0])
    
    for si in range(2,num_steps):
        min_cost[si] = min(min_cost[si - 1] + abs(steps[si-1] - steps[si]),min_cost[si - 2] + abs(steps[si-2] - steps[si]))

    print(min_cost[-1])
    
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
        input = """4
10 30 40 20"""
        output = """30"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """2
10 10"""
        output = """0"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """6
30 10 60 10 60 50"""
        output = """40"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()