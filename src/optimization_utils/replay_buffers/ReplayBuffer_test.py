import unittest
from .ReplayBuffer import ReplayBuffer

class ReplayBufferTest(unittest.TestCase):

    def test_buffer(self):
        buffer = ReplayBuffer()
        buffer.push(
            state=None,
            reward=1,
            action=2
        )
        sample = buffer.sample()
        assert sample.state == None
        assert sample.reward == 1
        assert sample.action == 2

    def test_buffer_action_1_priority(self):
        buffer = ReplayBuffer(
            priority=lambda x: 1 if x.action == 1 else 0 
        )
        buffer.push(
            state=None,
            reward=1,
            action=2
        )
        buffer.push(
            state=None,
            reward=1,
            action=1
        )
        sample = buffer.sample()
        assert sample.state == None
        assert sample.reward == 1
        assert sample.action == 1

    def test_muZero_priority(self):
        buffer = ReplayBuffer(
            priority=lambda x: (x.metadata['reward'] - x.metadata['search'])
        )
        buffer.push(
            state=None,
            reward=1,
            action=3,
            metadata={
                "reward":0,
                "search": 10
            }
        )
        buffer.push(
            state=None,
            reward=1,
            action=1,
            metadata={
                "reward":0,
                "search": 0
            }
        )
        sample = buffer.sample()
        assert sample.state == None
        assert sample.reward == 1
        assert sample.action == 3

if __name__ == '__main__':
    unittest.main()
