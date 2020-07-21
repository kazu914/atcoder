import sys
from io import StringIO
import unittest


def resolve():
    num_users, num_querys = list(map(int, input().split()))

    user_follows = [['N' for i in range(num_users)]for i in range(num_users)]

    for i in range(num_querys):
        query = list(map(int, input().split()))
        if query[0] == 1:
            user_follows[query[1] - 1][query[2] - 1] = 'Y'
        if query[0] == 2:
            for j in range(num_users):
                if user_follows[j][query[1] - 1] == 'Y':
                    user_follows[query[1] - 1][j] = 'Y'
        if query[0] == 3:

            user_a = query[1] - 1
            now_follows = [*user_follows[user_a]]

            for user_x in range(num_users):

                if now_follows[user_x] == 'Y':
                    for k in range(num_users):
                        if user_follows[user_x][k] == 'Y':
                            user_follows[user_a][k] = 'Y'

    for user in user_follows:
        print(*user, sep="")


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
        input = """6 7
1 1 2
1 2 3
1 3 4
1 1 5
1 5 6
3 1
2 6"""
        output = """NYYNYY
NNYNNN
NNNYNN
NNNNNN
NNNNNY
YNNNYN"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
