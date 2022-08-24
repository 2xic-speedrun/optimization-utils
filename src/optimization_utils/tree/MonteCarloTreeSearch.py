
from src.optimization_utils.tree.MonteCarloNode import MonteCarloNode


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

        child = [(action, node.score) for action, node in self.root.children.items()]
        child = sorted(child, key=lambda x: x[1])

        return child[0][0]

        