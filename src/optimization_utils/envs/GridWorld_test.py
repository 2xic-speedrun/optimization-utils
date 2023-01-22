import unittest
from .GridWorld import GridWorld
import numpy as np

class TestGridWorld(unittest.TestCase):
    def test_should_set_done(self):
        env = GridWorld(n=2)
        assert 3 in env.legal_actions
        env.play(3)
        assert 4 in env.legal_actions
        env.play(4)
        assert env.done  == True
        assert np.count_nonzero(env.state) == 1
