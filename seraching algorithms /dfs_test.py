import unittest
from .depth_first_search import Graph

class TestDFS(unittest.TestCase):

    def setUp(self):
        self.graph = Graph()

        self.graph.add_edge(0, 1)
        self.graph.add_edge(0, 5)
        self.graph.add_edge(1, 4)
        self.graph.add_edge(1, 2)
        self.graph.add_edge(4, 3)
        self.graph.add_edge(2, 3)

    def test_dfs(self):
        self.assertEqual(self.graph.depth_first_search(3), True)
        self.assertEqual(self.graph.depth_first_search(9), False)

