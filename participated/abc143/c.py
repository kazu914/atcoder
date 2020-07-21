import sys
from io import StringIO
import unittest

def resolve():
    n = int(input())

    targets = input()
    ans = 1

    for i in range(len(targets)-1):
        if targets[i] == targets[i+1]:
            pass
        else:
            ans += 1

    print(ans)
#resolve()

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
        input = """10
aabbbbaaca"""
        output = """5"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """5
aaaaa"""
        output = """1"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """20
xxzaffeeeeddfkkkkllq"""
        output = """10"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()