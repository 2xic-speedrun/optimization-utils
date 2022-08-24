# from  https://en.wikipedia.org/wiki/Monte_Carlo_tree_search#Exploration_and_exploitation
#       https://www.chessprogramming.org/UCT

import numpy as np


class UCT:
    def __init__(self) -> None:
        pass

    def calculate(self, child_win_count, child_visit_count, parent_visit_count, c=np.sqrt(2)):
        return (child_win_count / child_visit_count) + c * np.sqrt(
            np.log(
                parent_visit_count
                /
                child_visit_count
            )
        )
