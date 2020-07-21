
import sys
from io import StringIO
import unittest

class Contest:
    def __init__(self, member_cost,food_cost,k):
        self.member_cost = member_cost
        self.food_cost   = food_cost
        self.max_training_times = k
        
    def canAchieve(self,target):
        sum_training_times = 0
        for i in range(len(self.member_cost)):
            sum_training_times += max(0,self.member_cost[i] - target//self.food_cost[i])

        return  sum_training_times <= self.max_training_times
        


    def bisect(self,begin,end):
        if (end - begin <= 1 ):
            return end
        target = (begin + end)//2
        if self.canAchieve(target):
            return self.bisect(begin,target)

        else:
            return self.bisect(target,end)




def resolve():
    n,k  = map(int,input().split())
    
    member_cost = list(map(int,input().split()))

    food_cost = list(map(int,input().split()))
    member_cost.sort()
    food_cost.sort(reverse=True)
    total_cost = []
    for i in range(len(member_cost)):
        total_cost.append(member_cost[i]*food_cost[i])

    max_total_cost = max(total_cost)
    contest = Contest(member_cost,food_cost,k)
    print(contest.bisect(-1,max_total_cost))
        
            


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