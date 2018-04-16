from game.client.OXControllerNetworkClient import OXControllerNetworkClient
from game.client.gameFSM import GameFSM, Events
from game.common.messages import Messages


class OXGame:

    def __init__(self):
        self.__game_type, self.__game_mode_multiplayer = self.prompt_user_for_game_type()
        self.__message_handler = Messages(self.__game_type)
        self.controller = OXControllerNetworkClient()
        self.id = None
        self._in_game_result = None
        while not self.id:
            self.id = self._get_new_game_instance()

        self.fsm = GameFSM(self)

    def add_player(self, name, player_no):
        request = self.__message_handler. \
            create_request('add_player', self.id, player_name=name, player_number=player_no)
        return self.controller.get(request)

    def get_current_player(self):
        request = self.__message_handler.create_request('get_current_player', self.id)
        return self.controller.get(request)

    def get_board(self):
        request = self.__message_handler.create_request('get_board', self.id)
        return self.controller.get(request)

    def make_move(self, field):
        request = self.__message_handler.create_request('make_move', self.id, chosen_field=field)
        return self.controller.get(request)

    def _get_new_game_instance(self):
        request = self.__message_handler.create_request('get_new_game_instance', 0, mode=self.__game_mode_multiplayer)
        return self.controller.get(request)

    def check_game_result(self):
        request = self.__message_handler.create_request('check_game_result', self.id)
        result = self.controller.get(request)
        return result if result != 'False' else None

    def end_game(self):
        request = self.__message_handler.create_request('end_game', self.id)
        self.controller.get(request)

    def play(self):
        try:
            self.fsm.handle_event(Events.INIT_GAME)
            self.fsm.handle_event(Events.CONTINUE_GAME)
            self.fsm.handle_event(Events.FINISH_GAME)
        except EOFError:
            print('Quitting the game...')

    def init_players(self):
        player1 = input('Please enter yor name (Player 1)\n')
        self.add_player(player1, 0)
        if self.__game_mode_multiplayer:
            player2 = input('Please enter yor name (Player 2)\n')
            self.add_player(player2, 1)
        return None

    def perform_next_move(self):
        print(self.get_board())
        move_ok = None
        while not move_ok:
            move = input('Please choose next move\n')
            move_ok = self.make_move(move)
        self._in_game_result = self.check_game_result()
        if not self._in_game_result:
            self.fsm.handle_event(Events.CONTINUE_GAME)

    def finish_game(self):
        print('Game Over!')
        print(self.get_board())
        print('\n')
        print(self._in_game_result)
        self.end_game()
        print('Thank you.')
        return None

    def prompt_user_for_game_type(self):
        game_types = ['ox', 'interval']
        out_game = None
        multi_player = False
        while out_game not in game_types:
            print('\nSelect game number\n 0 - Tic Tac Toe\n 1 - Intervals')
            choice = input()
            if '0' != choice and choice != '1':
                continue
            out_game = game_types[int(choice)]
        if out_game == 'ox':
            choice = input('If you want to play in multiplayer mode please press enter, else type N\n')
            multi_player = len(choice) == 0

        return out_game, multi_player


if __name__ == '__main__':
    game = OXGame()
    game.play()
