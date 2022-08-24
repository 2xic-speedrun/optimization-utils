import unittest
from .TicTacToe import TicTacToe

class TestTicTacToe(unittest.TestCase):

    def test_tic_tac_toe(self):
        tic_tac_toe = TicTacToe()
        tic_tac_toe.play(2)
        assert tic_tac_toe.state[0][2] == 1
        tic_tac_toe.play(1)
        assert tic_tac_toe.state[0][1] == -1
        tic_tac_toe.play(8)
        assert tic_tac_toe.state[2][2] == 1
        tic_tac_toe.play(6)
        assert tic_tac_toe.state[2][0] == -1

    def test_tic_tac_toe_winner(self):
        tic_tac_toe = TicTacToe()

        tic_tac_toe.play(0)
        tic_tac_toe.play(tic_tac_toe.n + 1)

        tic_tac_toe.play(tic_tac_toe.n)
        tic_tac_toe.play(5)

        tic_tac_toe.play(2 * tic_tac_toe.n)

        assert tic_tac_toe.winner == 1

if __name__ == '__main__':
    unittest.main()
