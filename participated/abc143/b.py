import sys
from io import StringIO
import unittest

def resolve():
    n = int(input())

    targets = list(map(int,input().split()))

    ans = 0
    for i in range(len(targets)):
        for j in range(i+1,len(targets)):
            ans += targets[i]*targets[j]
            #print(i,j)

    print(ans)

resolve()

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
3 1 2"""
        output = """11"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """7
5 0 7 8 3 3 2"""
        output = """312"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()