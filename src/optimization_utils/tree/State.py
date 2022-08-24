import abc
from copy import deepcopy

class State:
    def __init__(self, state) -> None:
        self.state = deepcopy(state)

    @abc.abstractproperty
    def possible_actions_count(self):
        pass

    @abc.abstractproperty
    def is_terminator_state(self):
        pass

    @abc.abstractclassmethod
    def transition(self, action):
        pass

    @abc.abstractclassmethod
    def reward(self):
        pass
