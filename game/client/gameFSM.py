from game.common.enums.Events import Events
from game.common.enums.GameStatus import GameStatus


class Transition:
    def __init__(self, given_state, next_state, action):
        self.given_state = given_state
        self.next_state = next_state
        self.action = action


class GameFSM:
    def __init__(self, game):
        self.__state = GameStatus.INIT
        self.__game = game
        self.__transitions = {
            Events.INIT_GAME: Transition(GameStatus.INIT, GameStatus.IN_GAME, self.__game.init_players),
            Events.CONTINUE_GAME: Transition(GameStatus.IN_GAME, GameStatus.IN_GAME, self.__game.perform_next_move),
            Events.FINISH_GAME: Transition(GameStatus.IN_GAME, GameStatus.END_GAME, self.__game.finish_game)
        }

    def handle_event(self, event):
        self.__state = self.__transitions[event].next_state
        self.__transitions[event].action()
