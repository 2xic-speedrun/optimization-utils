import unittest
from optimization_utils.envs.SimpleEnv import SimpleEnv

from optimization_utils.tree.MuzeroMonteCarloNode import MuzeroMonteCarloNode
from optimization_utils.tree.MuzeroSimpleEnvState import MuzeroSimpleEnvState

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
        for _ in range(5):
            tree.step()
            if tree.root.score != 0:
                break
        assert tree.root.score != 0

    def test_tic_tac_toe_select_best_action(self):
        tic_tac_toe = TicTacToe()
        tic_tac_toe.play(0)
        tic_tac_toe.play(4)
        tic_tac_toe.play(3)
        tic_tac_toe.play(5)

        tree = MonteCarloTreeSearch(
            TicTacToeState(tic_tac_toe)
        )
        assert tree.get_action() is not None

    def test_should_be_possible_to_select_another_node_type(self):
        simple_state_env = SimpleEnv()
        def dynamics_function(state, action): return (1, None)

        tree = MonteCarloTreeSearch(
            MuzeroSimpleEnvState(simple_state_env, dynamics=dynamics_function,
                                 legal_actions=simple_state_env.legal_actions, action_space=simple_state_env.action_space),
            node=MuzeroMonteCarloNode,
        )
        for _ in range(100):
            tree.step()

        assert tree.get_action() is not None
        assert tree.root.muzero_action is not None


if __name__ == '__main__':
    unittest.main()
