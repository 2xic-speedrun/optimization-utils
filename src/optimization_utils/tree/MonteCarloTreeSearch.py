from optimization_utils.tree.MonteCarloNode import MonteCarloNode
import numpy as np


class MonteCarloTreeSearch:
    def __init__(self, root_state, node=MonteCarloNode, **kwargs) -> None:
        self.root = node(None, root_state, **kwargs)
        self.iterations = 0

    def step(self):
        current_node = self.root
        while not current_node.state.is_terminator_state:
            current_node = current_node.select()
        
        if current_node.state.is_terminator_state:
            current_node = current_node.backpropagation(
                current_node.state.reward)
        else:
            current_node = current_node.expand()
        self.iterations += 1

    def get_action(self, iterations=1000):
        for _ in range(iterations):
            self.step()

        child_nodes = [(action, node.score)
                 for action, node in self.root.children.items()]
        
        child_nodes = sorted(child_nodes, key=lambda x: x[1])

        return child_nodes[0][0]

    """
    Used for muzero, should probably be moved
    """
    @property
    def muzero_policy(self):
        assert self.iterations > 0
        return self.root.policy

    @property
    def muzero_value(self):
        assert self.iterations > 0
        return 1
