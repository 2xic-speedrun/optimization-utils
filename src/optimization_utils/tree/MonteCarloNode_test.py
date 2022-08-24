import unittest

from src.optimization_utils.tree.MonteCarloTreeSearch import MonteCarloTreeSearch
from src.optimization_utils.tree.State import State
from src.optimization_utils.tree.TicTacToeState import TicTacToeState

from ..envs.TicTacToe import TicTacToe

class TestMonteCarloNode(unittest.TestCase):

    def test_tic_tac_toe_first_iterate(self):
        tic_tac_toe = TicTacToe()
        tic_tac_toe.play(0)
        tic_tac_toe.play(4)
        tic_tac_toe.play(3)
        tic_tac_toe.play(5)

        tree = MonteCarloTreeSearch(
            TicTacToeState(tic_tac_toe)
        )
        # could select a path result in draw, so we do a few rollout
        for i in range(5):
            tree.step()
            if tree.root.score != 0:
                break
        assert tree.root.score != 0

    def tic_tac_toe_select_best_action(self):
        tic_tac_toe = TicTacToe()
        tic_tac_toe.play(0)
        tic_tac_toe.play(4)
        tic_tac_toe.play(3)
        tic_tac_toe.play(5)

        tree = MonteCarloTreeSearch(
            TicTacToeState(tic_tac_toe)
        )
        assert 6 == tree.get_action()


if __name__ == '__main__':
    unittest.main()
