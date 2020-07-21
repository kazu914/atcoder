import sys
from io import StringIO
import unittest


def resolve():
    n, m, q = map(int, input().split())
    graph = [[] for i in range(n)]
    for i in range(m):
        u, v = map(int, input().split())
        graph[u-1].append(v-1)
        graph[v-1].append(u-1)

    colors = list(map(int, input().split()))

    for i in range(q):
        query = list(map(int, input().split()))
        if (query[0] == 1):
            x = query[1] - 1
            print(colors[x])
            for z in graph[x]:
                colors[z] = colors[x]
        elif (query[0] == 2):

            x = query[1] - 1
            y = query[2]
            print(colors[x])

            colors[x] = y


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
        input = """3 2 3
1 2
2 3
5 10 15
1 2
2 1 20
1 1"""
        output = """10
10
20"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """30 10 20
11 13
30 14
6 4
7 23
30 8
17 4
6 23
24 18
26 25
9 3
18 4 36 46 28 16 34 19 37 23 25 7 24 16 17 41 24 38 6 29 10 33 38 25 47 8 13 8 42 40
2 1 9
1 8
1 9
2 20 24
2 26 18
1 20
1 26
2 24 31
1 4
2 21 27
1 25
1 29
2 10 14
2 2 19
2 15 36
2 28 6
2 13 5
1 12
1 11
2 14 43"""
        output = """18
19
37
29
8
24
18
25
46
10
18
42
23
4
17
8
24
7
25
16"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
