import sys
from io import StringIO
import unittest


def resolve():
    n, m, q = map(int, input().split())
    user_solved = [[0 for j in range(m)]for i in range(n)]
    solved = [0 for i in range(m)]

    for _ in range(q):
        query = list(map(int, input().split()))
        if query[0] == 1:  # 出力
            user = query[1] - 1
            score = 0
            for i in range(len(user_solved[user])):
                score += user_solved[user][i] * (n - solved[i])
            print(score)
        else:
            user = query[1] - 1
            question = query[2]-1
            user_solved[user][question] = 1
            solved[question] += 1


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
        input = """2 1 6
2 1 1
1 1
1 2
2 2 1
1 1
1 2"""
        output = """1
0
0
0"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """5 5 30
1 3
2 3 5
1 3
2 2 1
2 4 5
2 5 2
2 2 3
1 4
2 4 1
2 2 2
1 1
1 5
2 5 3
2 4 4
1 4
1 2
2 3 3
2 4 3
1 3
1 5
1 3
2 1 3
1 1
2 2 4
1 1
1 4
1 5
1 4
1 1
1 5"""
        output = """0
4
3
0
3
10
9
4
4
4
0
0
9
3
9
0
3"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
