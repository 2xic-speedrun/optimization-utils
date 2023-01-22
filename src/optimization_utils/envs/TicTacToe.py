import numpy as np
from copy import deepcopy
import random

class TicTacToe:
    def __init__(self, n=3, is_auto_mode=False) -> None:
        self.is_auto_mode = is_auto_mode
        self.n = n
        self.reset()

    def reset(self):
        n = self.n
        self.state = np.zeros((n, n))
        # player 1 and -1
        self.player = 1
        self.legal_actions = list(range(n * n))
        self.n = n
        self.done = False
        self.action_space = n * n
     #   self.reward = 0

    def soft_apply(self, action):
        state = self.state.copy()
        state = self.apply_action(action, state)
        return state

    def play(self, action):
        if self.done:
            raise Exception("Game is done.")

        if action in self.legal_actions:
            self.state = self.apply_action(action, self.state)
            self.switch_player()

            self.legal_actions.remove(action)
            self.done = self.winner is not None or len(self.legal_actions) == 0

            if self.is_auto_mode and self.player == -1 and not self.done:
                self.play(random.sample(self.legal_actions, k=1)[0])
        else:
            raise Exception(f"Illegal action by {self.player} by action {action}")
        
        return (
            self.winner if self.winner is not None else 0
        )

    def apply_action(self, action, state):
        if action in self.legal_actions:
            x = action % self.n
            y = action // self.n

            state[y][x] = self.player

            return state
        else:
            raise Exception(f"Illegal action by {self.player} by action {action}")

    def switch_player(self):
        self.player *= -1

    @property
    def winner(self):
        for i in range(self.n):
            if abs(sum(self.state[:, i])) == self.n:
                return self.state[:, i][0]
            elif abs(sum(self.state[i, :])) == self.n:
                return self.state[i, :][0]
        return None

    def __str__(self) -> str:
        return str(self.state)
