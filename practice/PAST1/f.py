import sys
from io import StringIO
import unittest


def resolve():
    S = input()
    cap = 0
    words = []
    word = ''
    for s in S:
        word += s
        if s.isupper():
            cap += 1
        if cap == 2:
            words.append(word.lower())
            cap = 0
            word = ''
    words.sort()
    anss = []
    for word in words:
        ans = word[0].upper()+word[1:len(word)-1] + word[-1].upper()
        anss.append(ans)

    print(*anss, sep='')


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
        input = """FisHDoGCaTAAAaAAbCAC"""
        output = """AAAaAAbCACCaTDoGFisH"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """AAAAAjhfgaBCsahdfakGZsZGdEAA"""
        output = """AAAAAAAjhfgaBCsahdfakGGdEZsZ"""
        self.assertIO(input, output)


if __name__ == "__main__":
    unittest.main()
