import os
from DiGraph import DiGraph
from GraphAlgo import GraphAlgo
from Meta import UpdateInformalInterface
import unittest
from random import randint as rand
import time
import sys


def check():
    """
    Graph: |V|=4, |E|=5
    {0: 0: |edges_out| 1 |edges in| 1, 1: 1: |edges_out| 3 |edges in| 1, 2: 2: |edges_out| 1 |edges in| 1, 3: 3: |edges_out| 0 |edges in| 2}
    {0: 1}
    {0: 1.1, 2: 1.3, 3: 10}
    (3.4, [0, 1, 2, 3])
    (2.8, [0, 1, 3])
    (inf, [])
    (None, inf)
    2.062180280059253 [1, 10, 7]
    17.693921758901507 [47, 46, 44, 43, 42, 41, 40, 39, 15, 16, 17, 18, 19]
    11.51061380461898 [20, 21, 32, 31, 30, 29, 14, 13, 3, 2]
    inf []
    ([1, 9, 2, 3], 2.370613295323088)
    (None, inf)
    ([1, 2, 3, 4], 4.5)
    """

    check0()
    check1()
    check2()
    check3()
    check_test()
    check_scales()


def check0():
    """
    This function tests the naming (main methods of the DiGraph class, as defined in GraphInterface.
    :return:
    """
    g = DiGraph()  # creates an empty directed graph
    for n in range(4):
        g.add_node(n)
    g.add_edge(0, 1, 1)
    g.add_edge(1, 0, 1.1)
    g.add_edge(1, 2, 1.3)
    g.add_edge(2, 3, 1.1)
    g.add_edge(1, 3, 1.9)
    g.remove_edge(1, 3)
    g.add_edge(1, 3, 10)
    print(g)  # prints the __repr__ (func output)
    print(g.get_all_v())  # prints a dict with all the graph's vertices.
    print(g.all_in_edges_of_node(1))
    print(g.all_out_edges_of_node(1))
    g_algo = GraphAlgo(g)
    print(g_algo.shortest_path(0, 3))
    g_algo.plot_graph()


def check1():
    """
       This function tests the naming (main methods of the GraphAlgo class, as defined in GraphAlgoInterface.
    :return:
    """
    g_algo = GraphAlgo()  # init an empty graph - for the GraphAlgo
    file = "../data/T0.json"
    g_algo.load_from_json(file)  # init a GraphAlgo from a json file
    print(g_algo.shortest_path(0, 3))
    print(g_algo.shortest_path(3, 1))
    print(g_algo.centerPoint())
    g_algo.save_to_json(file + '_saved')
    g_algo.plot_graph()


def check2():
    """ This function tests the naming, basic testing over A5 json file.
      :return:
      """
    g_algo = GraphAlgo()
    file = '../data/A5.json'
    g_algo.load_from_json(file)
    g_algo.get_graph().remove_edge(13, 14)
    g_algo.save_to_json(file + "_edited")
    dist, path = g_algo.shortest_path(1, 7)
    print(dist, path)
    dist, path = g_algo.shortest_path(47, 19)
    print(dist, path)
    dist, path = g_algo.shortest_path(20, 2)
    print(dist, path)
    dist, path = g_algo.shortest_path(2, 20)
    print(dist, path)
    print(g_algo.TSP([1, 2, 3]))
    g_algo.plot_graph()


def check3():
    """ This function tests the naming, basic testing over A5 json file.
      :return:
      """
    g = DiGraph()  # creates an empty directed graph
    for n in range(5):
        g.add_node(n)
    g.add_edge(0, 1, 1)
    g.add_edge(0, 4, 5)
    g.add_edge(1, 0, 1.1)
    g.add_edge(1, 2, 1.3)
    g.add_edge(1, 3, 1.9)
    g.add_edge(2, 3, 1.1)
    g.add_edge(3, 4, 2.1)
    g.add_edge(4, 2, .5)
    g_algo = GraphAlgo(g)
    print(g_algo.centerPoint())
    print(g_algo.TSP([1, 2, 4]))
    g_algo.plot_graph()


def check_test():
    """ This function runs the UnitTesting"""
    g_test = TestDiGraph()
    g_test.test_all()
    g_algo_test = TestGraphAlgo()
    g_algo_test.test_all()
    print("tested all")


def check_scales():
    x = 1000
    while x <= 1000000:
        g = DiGraph()
        for i in range(x):
            g.add_node(i)
        for i in range(20):
            n1 = rand(0, x)
            n2 = rand(0, x)
            while n2 == n1:
                n2 = rand(0, x)
            g.add_edge(n1, n2, rand(0, x))

        algo = GraphAlgo(g)

        print("x = ", x)

        start = time.time()
        print("Save: ", end="")
        algo.save_to_json("temp.json")
        stop_timer(start)

        start = time.time()
        print("Load: ", end="")
        algo.load_from_json("temp.json")
        stop_timer(start)

        os.remove("temp.json")

        # start = time.time()
        # print("Shortest path between 2 random vertices: ", end="")
        # algo.shortest_path(rand(0, x), rand(0, x))
        # stop_timer(start)

        # start = time.time()
        # print("Center: ", end="")
        # algo.centerPoint()
        # stop_timer(start)

        # cities = []
        # for i in range(20):
        #     v = rand(0, x)
        #     while v in cities:
        #         v = rand(0, x)
        #     cities.append(v)
        # start = time.time()
        # print("TSP (with 20 random cities): ", end="")
        # algo.TSP(cities)
        # stop_timer(start)

        start = time.time()
        print("Plotting: ", end="")
        algo.plot_graph()
        stop_timer(start)

        x *= 10


def stop_timer(start):
    print(time.time() - start, end="s\n")


class TestDiGraph(unittest.TestCase):

    def __init__(self):
        super().__init__()
        g = DiGraph()  # creates an empty directed graph
        for n in range(4):
            g.add_node(n)
        g.add_edge(0, 1, 1)
        g.add_edge(1, 0, 1.1)
        g.add_edge(1, 2, 1.3)
        g.add_edge(2, 3, 1.1)
        g.add_edge(1, 3, 1.9)
        g.remove_edge(1, 3)
        g.add_edge(1, 3, 10)
        self.g = g
        self.mc = 11

    def test_subclass(self):
        self.assertTrue(issubclass(type(self.g), UpdateInformalInterface))

    def test_sizes(self):
        self.assertEqual(self.g.v_size(), 4)
        self.assertEqual(self.g.e_size(), 5)

    def test_nodes(self):
        if self.g.v_size() > 0:
            j = 0
            for i in self.g.get_all_v().keys():
                self.assertEqual(j, i)
                j += 1

    def test_edges(self):
        if self.g.v_size() > 0:
            for i in self.g.get_all_v():
                if self.g.all_out_edges_of_node(i):
                    for j in self.g.all_out_edges_of_node(i).items():
                        self.assertEqual(j[1], self.g.all_in_edges_of_node(j[0])[i])
                if self.g.all_in_edges_of_node(i):
                    for j in self.g.all_in_edges_of_node(i).items():
                        self.assertEqual(j[1], self.g.all_out_edges_of_node(j[0])[i])

    def test_mc(self):
        self.assertEqual(self.mc, self.g.get_mc())

    def test_add(self):
        self.assertFalse(self.g.add_edge(0, 1, 1))
        for i in range(4):
            self.assertFalse(self.g.add_node(0))
        self.assertTrue(self.g.add_node(4))
        self.mc += 1
        self.assertTrue(self.g.add_edge(4, 2, 30))
        self.mc += 1

    def test_remove(self):
        self.assertFalse(self.g.remove_node(10))
        self.assertFalse(self.g.remove_edge(4, 1))
        self.assertTrue(self.g.remove_node(4))
        self.mc += 1
        self.assertFalse(self.g.remove_edge(4, 2))

    def test_all(self):
        self.test_subclass()
        self.test_sizes()
        self.test_nodes()
        self.test_edges()
        self.test_mc()
        self.test_add()
        self.test_remove()
        self.test_mc()


class TestGraphAlgo(unittest.TestCase):

    def __init__(self):
        super().__init__()
        g = DiGraph()  # creates an empty directed graph
        for n in range(5):
            g.add_node(n)
        g.add_edge(0, 1, 1)
        g.add_edge(0, 4, 5)
        g.add_edge(1, 0, 1.1)
        g.add_edge(1, 2, 1.3)
        g.add_edge(1, 3, 1.9)
        g.add_edge(2, 3, 1.1)
        g.add_edge(3, 4, 2.1)
        g.add_edge(4, 2, .5)
        g_algo = GraphAlgo(g)
        self.g_algo = g_algo
        self.testing_save_and_load = False

    def test_subclass(self):
        self.assertTrue(issubclass(type(self.g_algo), UpdateInformalInterface))

    def test_shortest_path(self):
        g = self.g_algo.get_graph()
        g.remove_edge(0, 4)
        g.add_edge(0, 4, 5.01)
        self.assertEqual(self.g_algo.shortest_path(0, 4)[0], 5)
        self.assertEqual(self.g_algo.shortest_path(0, 4)[1], [0, 1, 3, 4])
        g.remove_edge(0, 4)
        g.add_edge(0, 4, 4.99)
        self.assertEqual(self.g_algo.shortest_path(0, 4)[0], 4.99)
        self.assertEqual(self.g_algo.shortest_path(0, 4)[1], [0, 4])
        self.assertEqual(self.g_algo.shortest_path(4, 0)[0], float("inf"))
        g.remove_edge(0, 4)
        g.add_edge(0, 4, 5)

    def test_tsp(self):
        g = self.g_algo.get_graph()
        g.remove_edge(2, 3)
        g.add_edge(2, 3, 1.11)
        self.assertEqual(self.g_algo.TSP([0, 1, 2, 3, 4])[0], [0, 1, 3, 4, 2])
        self.assertEqual(self.g_algo.TSP([0, 1, 2, 3, 4])[1], 5.5)
        g.remove_edge(2, 3)
        g.add_edge(2, 3, 1.09)
        self.assertEqual(self.g_algo.TSP([0, 1, 2, 3, 4])[0], [0, 1, 2, 3, 4])
        self.assertEqual(self.g_algo.TSP([0, 1, 2, 3, 4])[1], 5.49)
        g.remove_edge(2, 3)
        g.remove_edge(3, 4)
        self.assertEqual(self.g_algo.TSP([0, 1, 2, 3, 4])[1], float("inf"))
        g.add_edge(2, 3, 1.1)
        g.add_edge(3, 4, 2.1)

    def test_center_point(self):
        self.assertEqual(self.g_algo.centerPoint()[0], None)
        g = self.g_algo.get_graph()
        g.add_edge(4, 0, 5)
        self.assertEqual(self.g_algo.centerPoint()[0], 1)
        self.assertEqual(self.g_algo.centerPoint()[1], 4)
        g.remove_edge(4, 0)

    def test_plot_graph(self):
        g = DiGraph()
        g.add_node(0, (1, 1, 0))
        g.add_node(1, (3, 1, 0))
        g.add_edge(0, 1, 1)
        g_algo = GraphAlgo(g)
        g_algo.plot_graph()
        g.add_edge(1, 0, 1)
        g.add_node(2, (2, .5, 0))
        g.add_edge(0, 2, 1)
        g.add_edge(2, 1, 1)
        g_algo.plot_graph()

    def test_save_and_load(self):
        if not self.testing_save_and_load:
            self.testing_save_and_load = True
            self.g_algo.save_to_json("temp_g")
            self.g_algo.load_from_json("temp_g")
            self.test_all()
            os.remove("temp_g.json")

    def test_all(self):
        self.test_subclass()
        self.test_shortest_path()
        self.test_tsp()
        self.test_center_point()
        self.test_plot_graph()


def plot(file_name):
    algo = GraphAlgo()
    algo.load_from_json(file_name)
    algo.plot_graph()


if __name__ == '__main__':
    # check()
    plot(sys.argv[1])
