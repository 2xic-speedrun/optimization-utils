import numpy as np
import random

from optimization_utils.exploration.EpsilonGreedy import EpsilonGreedy

class EpsilonGreedyManual(EpsilonGreedy):
    def __init__(self, actions) -> None:
        EpsilonGreedy.__init__(self, actions)
        self.decay = 1

    def update(self, rate=0.998):
        self._update_epsilon(rate)
