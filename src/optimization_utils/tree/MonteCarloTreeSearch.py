from src.optimization_utils.tree.MonteCarloNode import MonteCarloNode
import numpy as np


class MonteCarloTreeSearch:
    def __init__(self, root_state) -> None:
        self.root = MonteCarloNode(None, root_state)

    def step(self):
        current_node = self.root
        while not current_node.state.is_terminator_state:
            current_node = current_node.select()

        if current_node.state.is_terminator_state:
            current_node = current_node.backpropagation(
                current_node.state.reward)
        else:
            current_node = current_node.expand()

    def get_action(self, iterations=1000):
        for _ in range(iterations):
            self.step()

        child = [(action, node.score)
                 for action, node in self.root.children.items()]
        child = sorted(child, key=lambda x: x[1])

        return child[0][0]

    """
    Used for muzero, should probably be moved
    """
    @property
    def muzero_policy(self):
        return self.root.policy

    @property
    def muzero_action(self):
        action_policy = [0, ] * self.root.action_space
        nodes_policy = self.root.policy
        nodes_visit_counts = self.root.visits

        c_1 = 1.25
        c_2 = 19_625

        for action, node in self.root.children.items():
            influence = (
                c_1 + np.log(
                    sum(nodes_visit_counts) + c_2 + 1
                ) /
                c_2
            )
            action_policy[action] = node.mean_value + nodes_policy[action] * (
                np.sqrt(sum(nodes_visit_counts))
            ) / (
                1 + nodes_visit_counts[action]
            ) * influence

        return np.argmax(action_policy)
