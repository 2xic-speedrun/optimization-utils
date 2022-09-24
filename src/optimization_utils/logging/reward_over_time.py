
"""
Just a basic rl mean reward tracker
"""

class RewardOverTime:
    def __init__(self) -> None:
        self.value = 0
        self.n = 1

    def update(self, reward):
        self.value += (reward - self.value) / (self.n + 1)
        self.n += 1
