from collections import defaultdict
from curses import meta


class Diagnostics:
    def __init__(self) -> None:
        self.action_distribution = defaultdict(int)
        self.rewards = []

    def profile(self, action):
        self.action_distribution[action] += 1

    def reward(self, reward):
        self.rewards.append(reward)

    def print(self, epoch, metadata={}):
        actions = list(self.action_distribution.values())
        actions_sum = sum(actions)
        actions = [round(i / actions_sum, 2) for i in actions]

        avg_reward = sum(self.rewards)/len(self.rewards)

        metadata["action usage"] = actions
        metadata["avg. reward"] = avg_reward

        string_metadata = ""
        for key, value in metadata.items():
            string_metadata += f"{key} : {value}\t"

        print(f"\t{epoch} " + string_metadata )

        self.action_distribution.clear()
        self.rewards = []
