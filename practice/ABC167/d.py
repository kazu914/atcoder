import sys
from io import StringIO
import unittest


def resolve():
    citys_num, k = map(int, input().split())
    cities = list(map(int, input().split()))

    visited = set()
    route = []
    isAgain = False
    currectCity = 1
    while not isAgain:
        if currectCity in visited:
            route.append(currectCity)

            isAgain = True
        else:
            visited.add(currectCity)
            route.append(currectCity)

            currectCity = cities[currectCity - 1]
    if len(route) > k:
        print(route[k])
        return
    loopstart = route.index(route[-1])
    loop = route[loopstart:-1]

    k = k - loopstart
    k = k % len(loop)

    print(loop[k])


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
        input = """4 5
3 2 4 1"""
        output = """4"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6 727202214173249351
6 5 2 5 3 2"""
        output = """2"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
