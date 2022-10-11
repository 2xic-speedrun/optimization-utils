from copy import deepcopy
from .State import State


class SimpleEnvState(State):
    def __init__(self, simplEnv, depth=0) -> None:
        super().__init__(simplEnv)
        self._reward = 0
        self.depth = depth

    @property
    def action_space(self):
        return self.state.action_space

    @property
    def possible_actions(self):
        return self.state.legal_actions

    @property
    def is_terminator_state(self):
        return self.depth > 5

    def transition(self, action):
        copy = deepcopy(self.state)
        
        _, reward, _, _ = copy.step(action)
        self._reward = reward

        return SimpleEnvState(copy, depth=self.depth+1)

    @property
    def reward(self):
        return self._reward
