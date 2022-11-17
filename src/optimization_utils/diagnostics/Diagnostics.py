from collections import defaultdict
from typing import Any
import torch

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
        metadata["last reward"] = self.rewards[-1]

        string_metadata = self._create_metadata_entry(metadata)
        
        for key, value in self.key_values.items():
            value = len(value)
            string_metadata += f"{key} : {value}"

        print(f"\t{epoch} " + string_metadata )

        self.action_distribution.clear()
        self.key_values.clear()
        self.rewards = []

    def model_print(self, metadata):
        print(f"\t  {self._create_metadata_entry(metadata)}")
        print()

    def _create_metadata_entry(self, metadata):
        string_metadata = ""
        for key, value in metadata.items():
            value = self._make_printable(value)
            string_metadata += f"{key} : {value}\t"
        return string_metadata

    def isValueChanging(self, key, value: Any):
        self.key_values[key][value] = 1

    def _make_printable(self, value):
        if torch.is_tensor(value) and len(value.shape) == 1:
            return self._format_float(value.item())
        elif type(value) == float:
            return self._format_float(value)
        return value

    def _format_float(self, x):
        return round(x, 4)

    """
    TODO: 
        - Rerun the same model x times, and see the variance in the reward etc.
    """

    """
    TODO:
        - Add option to dump the printed stats to a storage.
            - Allows for comparing runs etc.
    """