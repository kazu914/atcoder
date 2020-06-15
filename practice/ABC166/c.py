import sys
from io import StringIO
import unittest


def resolve():
    num_ten, num_load = map(int, input().split())
    hiehgts = list(map(int, input().split()))
    tenbos = [[]for i in range(num_ten)]
    ans = 0
    for i in range(num_load):
        a, b = map(int, input().split())
        tenbos[a-1].append(b-1)
        tenbos[b-1].append(a-1)

    for index in range(len(tenbos)):
        height = hiehgts[index]
        heightest = True

        for tenbo in tenbos[index]:
            if (hiehgts[tenbo] >= height):
                heightest = False
        if heightest:
            ans += 1

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
        input = """4 3
1 2 3 4
1 3
2 3
2 4"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6 5
8 6 9 1 2 1
1 3
4 2
4 3
4 6
4 6"""
        output = """3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
