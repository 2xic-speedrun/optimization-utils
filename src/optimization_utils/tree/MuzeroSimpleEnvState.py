from copy import deepcopy
from .State import State
import torch


class MuzeroSimpleEnvState(State):
    def __init__(self,
                 state_representation: torch.tensor,
                 dynamics,
                 action_space,
                 legal_actions,
                 depth=0) -> None:
        super().__init__(state_representation)
        self._reward = 0
        self.depth = depth
        self._actions = action_space
        self.legal_actions = legal_actions
        self.dynamics = dynamics

    @property
    def action_space(self):
        return self._actions

    @property
    def possible_actions(self):
        if self.legal_actions == None:
            return list(range(self.action_space))
        return self.legal_actions

    @property
    def is_terminator_state(self):
        return self.depth > 5

    def transition(self, action):
        action = torch.tensor([action]).reshape((1, -1))
        reward, next_state = self.dynamics(self.state, action)
        self._reward = reward

        return MuzeroSimpleEnvState(next_state, dynamics=self.dynamics, action_space=self.action_space, legal_actions=None, depth=self.depth+1)

    @property
    def reward(self):
        return self._reward
