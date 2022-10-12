import abc
from copy import deepcopy
import torch

class State:
    def __init__(self, state) -> None:
        self.state = deepcopy(state) if not torch.is_tensor(state) else state

    @abc.abstractproperty
    def possible_actions(self):
        pass

    @abc.abstractproperty
    def action_space(self):
        pass

    @property
    def possible_actions_count(self):
        return len(self.possible_actions)

    @abc.abstractproperty
    def is_terminator_state(self):
        pass

    @abc.abstractclassmethod
    def transition(self, action):
        pass

    @abc.abstractclassmethod
    def reward(self):
        pass
