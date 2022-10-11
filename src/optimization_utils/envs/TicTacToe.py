import numpy as np

class TicTacToe:
    def __init__(self, n=3) -> None:
        self.state = np.zeros((n, n))
        # player 1 and -1
        self.player = 1
        self.legal_actions = list(range(n * n))
        self.n = n
        self.done = False
        self.action_space = n * n

    def play(self, action):
        if self.done:
            raise Exception("Game is done.")

        if action in self.legal_actions:
            self.legal_actions.remove(action)
            x = action % self.n
            y = action // self.n

            self.state[y][x] = self.player

            self.switch_player()
            self.done = self.winner is not None
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

