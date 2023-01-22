import unittest
from .CliffWalking import CliffWalking

class TestCliffWalking(unittest.TestCase):
    def test_should_set_done(self):
        env = CliffWalking(n=3)
        assert env.play(4) == -100
        assert env.done  == True
    
    def test_should_give_correct_reward_round_hill(self):
        env = CliffWalking(n=3)
        assert env.play(3) == -1
        assert env.play(4) == -1
        assert env.play(4) == -1
        assert env.play(1) == -1
        assert env.done  == True
    