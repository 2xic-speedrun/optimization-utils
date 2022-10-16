import os
import json


class EpochRuns:
    def __init__(self, path):
        self.path = path
        self.information = self.load(path)
        self.epochs = {

        }

    def load(self, path):
        if os.path.isfile(path):
            with open(path, "r") as file:
                return json.load(file)
        return []

    def log(self, key, value, epoch):
        if not epoch in self.epochs:
            self.epochs[epoch] = {
                "iteration": 1,
            }

        delta = self.epochs[epoch].get(key, 0)
        self.epochs[epoch][key] = delta + \
            (value - delta)/self.epochs[epoch]["iteration"]
        self.epochs[epoch]["iteration"] += 1

    def fetch(self, key):
        return list(map(lambda x: x[key], self.information))

    def store(self):
        sorted_epochs = sorted(self.epochs.items(), key=lambda x: x[0])
        sorted_epochs = list(map(lambda x: x[1], sorted_epochs))
        with open(self.path, "w") as file:
            json.dump(sorted_epochs, file)
