from copy import deepcopy
from .State import State

class TicTacToeState(State):
    def __init__(self, tic_tac_toe) -> None:
        super().__init__(tic_tac_toe)

    @property
    def possible_actions_count(self):
        return self.state.legal_actions

    @property
    def is_terminator_state(self):
        return self.state.done or len(self.state.legal_actions) == 0

    def transition(self, action):
        copy = deepcopy(self.state)
        copy.play(action)
        return TicTacToeState(copy)

    @property
    def reward(self):
        if self.state.winner is not None:
            return self.state.winner
