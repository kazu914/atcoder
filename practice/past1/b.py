import sys
from io import StringIO
import unittest


def resolve():
    n = int(input())
    pre = int(input())
    for i in range(n - 1):
        sell = int(input())
        if(pre == sell):
            print('stay')
        elif(sell > pre):
            print('up '+str(sell - pre))
        else:
            print('down '+str(pre - sell))
        pre = sell


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
9
10
3
100
100
90
80
10
30
10"""
        output = """up 1
down 7
up 97
stay
down 10
down 10
down 70
up 20
down 20"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
