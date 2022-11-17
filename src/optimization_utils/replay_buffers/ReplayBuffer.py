from collections import namedtuple
import numpy as np

from .priority.uniform import uniform_priority


state = namedtuple('state_representation', 'state reward action metadata is_last_state id')

class ReplayBuffer:
    def __init__(self, state=state, n=10_000, priority=uniform_priority) -> None:
        self.history = []
        self.size = n
        self.state = state
        self.priority = priority
        
    def push(self, state, reward, action, is_last_state=False, metadata={}, id=-1):
        self.history.append(self.state(
            state=state,
            reward=reward,
            action=action,
            metadata=metadata,
            is_last_state=is_last_state,
            id=id
        ))

    # TODO: This should probably be written another way.
    #       This way is inefficient.
    def sample_trajectory(self):
        sample_id = self.sample().id
        return [
            i for i in self.history if i.id == sample_id
        ]

    def sample(self):
        p = [self.priority(i) for i in self.history]
        p_sum = sum(p)
        p = [i / p_sum for i in p]
        idx = np.random.choice(len(self.history), p=p)
        return self.history[idx]
