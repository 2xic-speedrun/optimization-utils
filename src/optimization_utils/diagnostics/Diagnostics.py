from collections import defaultdict
from curses import meta
from typing import Any


class Diagnostics:
    def __init__(self) -> None:
        self.action_distribution = defaultdict(int)
        self.rewards = []
        self.key_values = defaultdict(dict)

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
        
        for key, value in self.key_values.items():
            string_metadata += f"{key} : {len(value)}"

        print(f"\t{epoch} " + string_metadata )

        self.action_distribution.clear()
        self.key_values.clear()
        self.rewards = []

    def isValueChanging(self, key, value: Any):
        self.key_values[key][value] = 1

    """
    TODO: 
        - Rerun the same model x times, and see the variance in the reward etc.
    """

    """
    TODO:
        - Add option to dump the printed stats to a storage.
            - Allows for comparing runs etc.
    """