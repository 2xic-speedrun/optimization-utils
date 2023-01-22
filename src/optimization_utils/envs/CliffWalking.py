import numpy as np

class CliffWalking:
    def __init__(self, n) -> None:
        self.n = n
        self.end = n * 10
        self.action_space = 5
        self.reset()

    def reset(self):
        self.state = np.zeros((self.n, self.n))
        self.state[0, 1:-1] = 1
        self.x = 0
        self.y = 0
        self.step = 0
        self.state[self.x][self.y] = 2
        self.reward = 0

    def is_done(self):
        return (
            (self.x == 0) and 
            (self.y + 1 == self.n)
        )
    
    def play(self, action):
        reward = -1
        assert action in self.legal_actions

        self.state[self.x][self.y] = 0
        if action == 1:
            self.x -= 1
        elif action == 2:
            self.y -= 1
        elif action == 3:
            self.x += 1
        elif action == 4:
            self.y += 1

        if self.state[self.x][self.y] == 1: 
            reward = -100
            self.step = self.end 

        self.step += 1
        self.state[self.x][self.y] = 2
       
        return reward

    @property
    def done(self):
        return self.step > self.end or self.is_done()

    @property
    def legal_actions(self):
        action = []
        if 0 < self.x:
            action.append(1)
        if 0 < self.y:
            action.append(2)
        if self.x < (self.n - 1):
            action.append(3)
        if self.y < (self.n - 1):
            action.append(4)
        return action

    def __str__(self) -> str:
        return str(self.state)
