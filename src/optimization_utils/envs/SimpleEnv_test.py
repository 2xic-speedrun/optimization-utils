import unittest
from src.optimization_utils.envs.SimpleEnv import SimpleEnv

class TestSimpleEnv(unittest.TestCase):
    def test_should_execute(self):
        env = SimpleEnv()
        assert env.index == 0
        (_, reward, _, _) = env.step(0)
        assert env.index == 1
        assert reward.item() == 1
        (_, reward, _, _) = env.step(0)
        assert env.index == 0
        assert reward.item() == 0
        (_, reward, _, _) = env.step(0)
        assert reward.item() == 1

