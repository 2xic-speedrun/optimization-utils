import unittest
from .PageRank import PageRank

class TestPageRank(unittest.TestCase):

    def test_page_rank(self):
        instance = PageRank()
        instance.add_link('small_node', ['unknown_node'])
        instance.add_link('big_node', ['big_node', 'small_node', 'middle_node'])
        instance.add_link('middle_node', ['small_node', 'big_node'])

        instance.calculate()

        assert instance.node_rank['small_node'] < instance.node_rank['middle_node'] 

if __name__ == '__main__':
    unittest.main()
