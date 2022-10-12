from .MonteCarloNode import MonteCarloNode
import numpy as np 

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
        nodes_policy = self.policy
        nodes_visit_counts = self.visits

        c_1 = 1.25
        c_2 = 19_625

        for action, node in self.children.items():
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
