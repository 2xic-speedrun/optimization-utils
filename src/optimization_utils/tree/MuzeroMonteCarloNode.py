from ast import NodeVisitor
from cmath import inf
from .MonteCarloNode import MonteCarloNode
import numpy as np
import random

class MuzeroMonteCarloNode(MonteCarloNode):
    def __init__(self, parent, state) -> None:
        super().__init__(parent, state)

    def select(self):
        action = self.muzero_action
        if not action in self.children:
            self.children[action] = self.get_instance_type()(
                self,
                self.state.transition(action),
            )
#            self.unexplored_nodes.remove(action)
        return self.children[action]

    def get_instance_type(self):
        return MuzeroMonteCarloNode

    @property
    def muzero_action(self):
        action_policy = [0, ] * self.action_space
        nodes_policy = self.state._policy # .#policy
        nodes_visit_counts = self.visits

        c_1 = 1.25
        c_2 = 19_625

      #  print(nodes_visit_counts)

        if random.randint(0, 10) == 2:
            return random.sample(self.state.possible_actions, k=1)[0]

        for action in self.state.possible_actions:
            node = self.children[action] if action in self.children else None
            influence = (
                c_1 + np.log(
                    sum(map(lambda x: x + c_2 + 1, nodes_visit_counts))
                ) /
                c_2
            )
            node_value = (node.mean_value if node else 0)

            policy = (
                np.sqrt(sum(nodes_visit_counts))
            ) / (
                1 + nodes_visit_counts[action]
            )

            action_policy[action] = node_value + \
                nodes_policy[action] * policy * influence

        return np.argmax(action_policy)
