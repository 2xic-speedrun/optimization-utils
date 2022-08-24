
from .State import State
import random

class MonteCarloNode:
    def __init__(self, parent, state: State):
        self.state = state
        self.children = {

        }
        self.parent = parent
        self.unexplored_nodes = self.state.possible_actions_count

        # metadata
        self.score = 0

    def select(self):
        if len(self.unexplored_nodes):
            index = random.randint(0, len(self.unexplored_nodes) - 1)
            action = self.unexplored_nodes[index]
            if not action in self.children:
                self.children[action] = MonteCarloNode(self, self.state.transition(action))
                self.unexplored_nodes.remove(action)
            return self.children[action]
        else:
            return random.sample(self.children.values(), k=1)[0]

    def expand(self):
        new_node = self.select()
        if new_node.state.is_terminator_state:
            self.backpropagation(new_node.state.reward)
        else:
            new_node.expand()
         
    def backpropagation(self, R):
        current_node = self
        while current_node is not None:
            if R is not None:
                current_node.score += R
            current_node = current_node.parent
