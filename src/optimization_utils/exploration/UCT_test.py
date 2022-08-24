import unittest
from .UCT import UCT

class TestUCT(unittest.TestCase):

    def test_uct(self):
        score = UCT()
        assert score.calculate(
            0, 10,
            50
        ) < score.calculate(
            10, 10,
            50
        )
        assert score.calculate(
            1, 1,
            50
        ) > score.calculate(
            10, 10,
            50
        )
        
if __name__ == '__main__':
    unittest.main()
