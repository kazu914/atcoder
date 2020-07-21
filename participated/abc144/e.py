
import sys
from io import StringIO
import unittest

import heapq
class Heapq:
    def __init__(self, arr, desc=False):
        if desc:
            arr = [-a for a in arr]
        self.sign = -1 if desc else 1
        self.hq = arr
        heapq.heapify(self.hq)
 
    def pop(self):
        return heapq.heappop(self.hq) * self.sign
 
    def push(self, a):
        heapq.heappush(self.hq, a * self.sign)
 
    def top(self):
        return self.hq[0] * self.sign

def resolve():
    n,k  = map(int,input().split())
    
    member_cost = list(map(int,input().split()))
    food_cost = list(map(int,input().split()))

    member_cost.sort()
    food_cost.sort(reverse=True)
    total_cost = []
    for i in range(len(member_cost)):
        total_cost.append(member_cost[i]*food_cost[i])

    total_cost_heap = Heapq(total_cost,True)
    if k >= sum(member_cost):
        print(0)
    else:
        while k > 0:
            k -= 1
            max_cost  = total_cost_heap.pop()
            reduce_index = total_cost.index(max_cost)
            member_cost[reduce_index] -= 1
            total_cost[reduce_index] -= food_cost[reduce_index]
            total_cost_heap.push(total_cost[reduce_index])
        print(max(total_cost))
        
            
# resolve()


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
        input = """3 5
4 2 1
2 3 1"""
        output = """2"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """3 8
4 2 1
2 3 1"""
        output = """0"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """11 14
3 1 4 1 5 9 2 6 5 3 5
8 9 7 9 3 2 3 8 4 6 2"""
        output = """12"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()