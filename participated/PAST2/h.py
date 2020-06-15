import sys
from io import StringIO
import unittest


class Resolver:
    def __init__(self, hardles, times, l):
        self.hardles = set(hardles)
        self.times = times
        self.costs = [-1 for i in range(l+1)]
        self.target = l
        self.costs[0] = 0
        self.costs[1] = self.action1(0)
        if(l < 2):
            ans = min(self.costs[1],
                      self.costs[0] + 0.5*times[0]+0.5*times[1])
            print(int(ans))
            return
        self.costs[2] = min(self.costs[1] + self.action1(1), self.action2(0))
        if(l < 3):
            ans = min(self.costs[2],
                      self.costs[1] + 0.5*times[0]+0.5*times[1],
                      self.costs[0] + 0.5*times[0]+1.5*times[1])

            print(int(ans))
            return

        self.costs[3] = min(self.costs[1] + self.action2(1),
                            self.costs[2] + self.action1(2))
        if(l < 4):
            ans = min(self.costs[3],
                      self.costs[2] + 0.5*times[0]+0.5*times[1],
                      self.costs[1] + 0.5*times[0]+1.5*times[1],
                      self.costs[0] + 0.5*times[0]+2.5*times[1])

            print(int(ans))
            return
        self.costs[4] = min(self.costs[2] + self.action2(2),
                            self.costs[3] + self.action1(3),
                            self.costs[0] + self.action3(0))
        if(l < 5):
            ans = min(self.costs[4],
                      self.costs[3] + 0.5*times[0]+0.5*times[1],
                      self.costs[2] + 0.5*times[0]+1.5*times[1],
                      self.costs[1] + 0.5*times[0]+2.5*times[1])

            print(int(ans))
            return
        self.dp()
        self.outans()

    def action1(self, now_x):
        cost = self.times[0]
        additional = 0 if (now_x + 1) not in self.hardles else self.times[2]
        return cost + additional

    def action2(self, now_x):
        cost = self.times[0] + self.times[1]
        additional = 0 if (now_x + 2) not in self.hardles else self.times[2]
        return cost + additional

    def action3(self, now_x):
        cost = self.times[0] + 3*self.times[1]
        dditional = 0 if (now_x + 4) not in self.hardles else self.times[2]
        return cost + dditional

    def dp(self):
        for i in range(5, len(self.costs)):
            self.costs[i] = min(self.costs[i-2] + self.action2(i-2),
                                self.costs[i-1] + self.action1(i-1),
                                self.costs[i-4] + self.action3(i-4))

    def outans(self):
        ans = min(self.costs[self.target],
                  self.costs[self.target - 1] +
                  0.5 * self.times[0] + 0.5 * self.times[1],
                  self.costs[self.target - 2] +
                  0.5 * self.times[0] + 1.5 * self.times[1],
                  self.costs[self.target - 3] + 0.5 * self.times[0] + 2.5 * self.times[1])
        print(int(ans))


def resolve():
    n, l = map(int, input().split())
    hardles = list(map(int, input().split()))
    times = list(map(int, input().split()))

    resolver = Resolver(hardles, times, l)
    # print(resolver.costs[l])


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
        input = """2 5
1 4
2 2 20"""
        output = """10"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4 5
1 2 3 4
2 20 100"""
        output = """164"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """10 19
1 3 4 5 7 8 10 13 15 17
2 1000 10"""
        output = """138"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
