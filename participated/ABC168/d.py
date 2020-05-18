import sys
from io import StringIO
import unittest

from collections import deque


def resolve():
    n, m = map(int, input().split())
    ans = [-1 for i in range(n)]

    connections = [[] for i in range(n)]
    for i in range(m):
        a, b = map(int, input().split())
        connections[a-1].append(b-1)
        connections[b-1].append(a-1)

    # stack = []
    # connected_to_one = [*connections[0]]

    # for room in connected_to_one:
    #     ans[room] = 1

    #     connections[0].remove(room)
    #     connections[room].remove(0)

    #     stack.append(room)

    D = deque([0])
    visited = [False]*n
    visited[0] = True

    while D:
        room = D.popleft()

        for i in connections[room]:
            if visited[i]:
                continue
            visited[i] = True
            ans[i] = room + 1
            D.append(i)

    _ans = ans[1:]

    if -1 in _ans:
        print('No')
    else:
        print('Yes')
        for i in _ans:
            print(i)


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
        input = """4 4
1 2
2 3
3 4
4 2"""
        output = """Yes
1
2
2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """6 9
3 4
6 1
2 4
5 3
4 6
1 5
6 2
4 5
5 6"""
        output = """Yes
6
5
5
1
1"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
