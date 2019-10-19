import sys
from io import StringIO
import unittest


class Graph():

    def __init__(self):
        self.adjacency_dict = {}

    def add_vertex(self, v):
        self.adjacency_dict[v] = []

    def add_edge(self, v1, v2, cost):
        self.adjacency_dict[v1].append([v2, cost])
        self.adjacency_dict[v2].append([v1, cost])

    def get_route(self, v1, v2, ):

    def is_connected(self, v1, v2, fuel, charge):
        connected_city =[]
        for city in self.adjacency_dict[v1]:
            connected_city.append(city[0])
            if city[0] == v2:
                if fuel >= city[1]:
                    pass
                else:
                    charge += 1
        return charge







def resolve():
    n, m, gas = map(int, input().split())

    graph = Graph()
    for i in range(n):
        graph.add_vertex(str(i + 1))

    for i in range(m):
        v1, v2, cost = map(int, input().split())
        graph.add_edge(str(v1), str(v2), cost)

    q = int(input())
    queries = [[] for i in range(q)]

    for i in range(q):
        fromcity,distination = map(int, input().split())
        print(graph.is_connected(str(fromcity), str(distination), gas, 0))



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
        input = """3 2 5
1 2 3
2 3 3
2
3 2
1 3"""
        output = """0
1"""
        self.assertIO(input, output)
    def test_入力例_2(self):
        input = """4 0 1
1
2 1"""
        output = """-1"""
        self.assertIO(input, output)
    def test_入力例_3(self):
        input = """5 4 4
1 2 2
2 3 2
3 4 3
4 5 2
20
2 1
3 1
4 1
5 1
1 2
3 2
4 2
5 2
1 3
2 3
4 3
5 3
1 4
2 4
3 4
5 4
1 5
2 5
3 5
4 5"""
        output = """0
0
1
2
0
0
1
2
0
0
0
1
1
1
0
0
2
2
1
0"""
        self.assertIO(input, output)

if __name__ == "__main__":
    unittest.main()