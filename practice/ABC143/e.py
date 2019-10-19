import sys
from io import StringIO
import unittest

inf = 10**10


def resolve():
    n, m, gas = map(int, input().split())

    costs = [[inf for i in range(n)] for i in range(n)]

    for i in range(len(costs)):
        costs[i][i] = 0
    for i in range(m):
        v1, v2, cost = map(int, input().split())
        costs[v1 - 1][v2 - 1] = cost
        costs[v2 - 1][v1 - 1] = cost

    for k in range(n):
        for i in range(n):
            for j in range(n):
                costs[i][j] = min(costs[i][j], costs[i][k]+costs[k][j])

    cost_with_gas = [[inf for i in range(n)] for i in range(n)]

    for i in range(len(cost_with_gas)):
        cost_with_gas[i][i] = 0
    for i in range(len(cost_with_gas)):
        for j in range(i+1, len(cost_with_gas)):
            if gas - costs[i][j] >= 0:
                cost_with_gas[i][j] = 1
                cost_with_gas[j][i] = 1

    for k in range(n):
        for i in range(n):
            for j in range(n):
                cost_with_gas[i][j] = min(cost_with_gas[i][j], cost_with_gas[i][k]+cost_with_gas[k][j])

    q = int(input())

    for i in range(q):
        from_city, destination = map(int, input().split())
        ans = cost_with_gas[from_city-1][destination-1] -1 if cost_with_gas[from_city-1][destination-1] != inf else -1
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
        input = """3 2 5
1 2 3
2 3 3
2
3 2
1 3"""
        output = """0
1"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """4 0 1
1
2 1"""
        output = """-1"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """5 4 4
1 2 2
2 3 2
3 4 3
4 5 2
20
2 1
3 1
4 1
5 1
1 2
3 2
4 2
5 2
1 3
2 3
4 3
5 3
1 4
2 4
3 4
5 4
1 5
2 5
3 5
4 5"""
        output = """0
0
1
2
0
0
1
2
0
0
0
1
1
1
0
0
2
2
1
0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()