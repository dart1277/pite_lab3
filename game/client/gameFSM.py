from game.common.enums.Events import Events
from game.common.enums.GameStatus import GameStatus


class GameState:
    def __init__(self, action):
        self._action = action

    def handle_event(self, fsm, event):
        if event == Events.INIT_GAME:
            return self.init_game(fsm)
        elif event == Events.CONTINUE_GAME:
            return self.continue_game(fsm)
        elif event == Events.FINISH_GAME:
            return self.finish_game(fsm)
        elif event == Events.DISPOSE_GAME:
            return self.dispose_game(fsm)

    def perform_action(self):
        self._action()

    def init_game(self, fsm):
        pass

    def continue_game(self, fsm):
        pass

    def finish_game(self, fsm):
        pass

    def dispose_game(self, fsm):
        pass


class GameStateInit(GameState):
    def __init__(self, action):
        super().__init__(action)

    def init_game(self, fsm):
        self.perform_action()
        fsm.set_state(GameStatus.IN_GAME)


class GameStateContinue(GameState):
    def __init__(self, action):
        super().__init__(action)

    def continue_game(self, fsm):
        self.perform_action()

    def finish_game(self, fsm):
        fsm.set_state(GameStatus.END_GAME)


class GameStateEnd(GameState):
    def __init__(self, action):
        super().__init__(action)

    def dispose_game(self, fsm):
        self.perform_action()


class GameFSM:
    def __init__(self, game):
        self.__game = game
        self.__states = {
            GameStatus.INIT: GameStateInit(self.__game.init_players),
            GameStatus.IN_GAME: GameStateContinue(self.__game.perform_next_move),
            GameStatus.END_GAME: GameStateEnd(self.__game.finish_game)
        }
        self.__state = self.__states[GameStatus.INIT]

    def handle_event(self, event):
        return self.__state.handle_event(self, event)

    def set_state(self, new_state):
        self.__state = self.__states[new_state]
