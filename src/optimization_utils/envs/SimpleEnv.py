import torch

"""
Simple environment
"""

class SimpleEnv:
    def __init__(self) -> None:
        self.reset()
        self.legal_actions = [0, 1]
        self.action_space = 2
        self.state_size = 2

    def reset(self):
        self.env:torch.Tensor = torch.tensor([0, 0])
        self.index = 0
        self.env[self.index] = 1
        self.timeout = 10
        return self

    def step(self, action):
        state = self.env.clone()
        reward = torch.tensor([0])
        if action == self.index:
            reward = torch.tensor([1])
        assert action < self.action_space

        self.env[self.index] = 0
        self.index = (self.index + 1) % 2
        self.env[self.index] = 1
        self.timeout -= 1

        return (
            state,
            reward,
            action,
            # gamma = 1 for now
            torch.tensor([1])
        )

    @property
    def state(self):
        return self.env

    def done(self):
        return self.timeout < 0
        
