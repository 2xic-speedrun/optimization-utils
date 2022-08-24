import unittest
from .EpsilonGreedy import EpsilonGreedy

class TestEpsilonGreedy(unittest.TestCase):

    def test_epsilon(self):
        action_sampler = EpsilonGreedy(3)
        action_sampler.get_action(lambda: 10)
        assert action_sampler.epsilon != 1

    def test_epsilon_decay_limit(self):
        action_sampler = EpsilonGreedy(3)
        action_sampler.decay = 0.1
        for _ in range(10):
            action_sampler.get_action(lambda: 10)
        assert action_sampler.epsilon > 0
        
if __name__ == '__main__':
    unittest.main()
