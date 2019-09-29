import sys
from io import StringIO
import unittest


def resolve():
    N = int(input())
    odd = 0
    even = 0
    for i in range(1,N+1):
        if(i%2==0):
            even +=1
        else:
            odd +=1
    print(odd/(odd+even))




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
        input = """4"""
        output = """0.5000000000"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """5"""
        output = """0.6000000000"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """1"""
        output = """1.0000000000"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()