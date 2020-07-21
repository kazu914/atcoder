import sys
from io import StringIO
import unittest


def resolve():
    n = int(input())
    ans = ''
    str_list = []
    for i in range(5):
        s1 = list(input().split())
        str_list.append(s1)
    for i in range(n):
        start = 4 * (i)
        # print(str_list[0][0][start:start+4])
        if str_list[0][0][start:start+4] == '..#.':
            ans += '1'
        elif str_list[0][0][start:start+4] == '.#.#':
            ans += '4'
        elif str_list[2][0][start:start+4] == '...#':
            ans += '7'
        elif str_list[3][0][start:start+4] == '.#..':
            ans += '2'
        elif str_list[1][0][start:start+4] == '.#..':
            if str_list[3][0][start:start+4] == '...#':
                ans += '5'
            else:
                ans += '6'
        elif str_list[1][0][start:start+4] == '...#':
            ans += '3'
        elif str_list[2][0][start:start+4] == '.#.#':
            ans += '0'
        elif str_list[3][0][start:start+4] == '.#.#':
            ans += '8'
        else:
            ans += '9'
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
        input = """10
.###..#..###.###.#.#.###.###.###.###.###.
.#.#.##....#...#.#.#.#...#.....#.#.#.#.#.
.#.#..#..###.###.###.###.###...#.###.###.
.#.#..#..#.....#...#...#.#.#...#.#.#...#.
.###.###.###.###...#.###.###...#.###.###."""
        output = """0123456789"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """29
.###.###.###.###.###.###.###.###.###.#.#.###.#.#.#.#.#.#.###.###.###.###..#..###.###.###.###.###.#.#.###.###.###.###.
...#.#.#...#.#.#.#.#.#...#.#...#.#.#.#.#.#...#.#.#.#.#.#.#.....#.#.#.#.#.##..#.#...#.#.#...#.#...#.#...#.#.....#...#.
.###.#.#...#.###.#.#.###.###...#.###.###.###.###.###.###.###...#.###.#.#..#..###...#.###.###.###.###.###.###.###.###.
.#...#.#...#...#.#.#.#.#...#...#.#.#...#.#.#...#...#...#.#.#...#...#.#.#..#..#.#...#...#.#...#.#...#.#.....#...#.#...
.###.###...#.###.###.###.###...#.###...#.###...#...#...#.###...#.###.###.###.###...#.###.###.###...#.###.###.###.###."""
        output = """20790697846444679018792642532"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
