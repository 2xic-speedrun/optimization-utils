import numpy as np
import random

class EpsilonGreedy:
    def __init__(self, actions) -> None:
        self.epsilon = 1
        self.epsilon_limit = 0.05
        self.decay = 0.998
        self.actions = actions

    def get_action(self, get_model_best_action):
        if np.random.rand() < self.epsilon:
            action = random.randint(0, self.actions)
            self._update_epsilon(self.decay)
            return action
        return get_model_best_action()

    def _update_epsilon(self, decay):
        if self.epsilon_limit < self.epsilon:
            self.epsilon *= decay
            