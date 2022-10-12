
from typing import Dict
from .State import State
import random

class MonteCarloNode:
    def __init__(self, parent, state: State):
        self.state = state
        self.children:Dict[int, MonteCarloNode] = {

        }
        self.parent = parent
        self.unexplored_nodes = self.state.possible_actions
        self.action_space = self.state.action_space

        # parameters
        self.T = 0.25

        # metadata
        self.score = 0
        self.visit_count = 0
        self.mean_value = 0
        self.reward = 0

    def get_instance_type(self):
        return MonteCarloNode

    def select(self):
        if len(self.unexplored_nodes):
            index = random.randint(0, len(self.unexplored_nodes) - 1)
            action = self.unexplored_nodes[index]
            if not action in self.children:
                self.children[action] = self.get_instance_type()(
                    self, self.state.transition(action))
                self.unexplored_nodes.remove(action)
            return self.children[action]
        else:
            return random.sample(list(self.children.values()), k=1)[0]

    def expand(self):
        new_node = self.select()
        if new_node.state.is_terminator_state:
            self.backpropagation(new_node.state.reward)
        else:
            new_node.expand()

    def backpropagation(self, R):
        current_node = self

        while current_node is not None:
            current_node.score += R
            self.mean_value = ((
                current_node.visit_count * self.mean_value
            ) + R) / (self.visit_count + 1)
            current_node.visit_count = current_node.visit_count + 1
            current_node = current_node.parent

    @property
    def policy(self):
        visits = [0, ] * self.action_space
        for key, value in self.children.items():
            visits[key] = value.visit_count ** (1/self.T)
        sum_visits = sum(visits)
        return [(v/sum_visits if v != 0 else 0) for v in visits]

    @property
    def visits(self):
        visits = [0, ] * self.action_space
        for key, value in self.children.items():
            visits[key] = value.visit_count
        return visits
