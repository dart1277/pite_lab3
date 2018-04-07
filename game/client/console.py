from game.client.OXControllerNetworkClient import OXControllerNetworkClient
from game.common.messages import Messages


class OXGame:

    def __init__(self):
        self.__game_type = 'ox'
        self.__game_mode_multiplayer = True
        self.__message_handler = Messages(self.__game_type)
        self.controller = OXControllerNetworkClient()
        self.id = None
        while not self.id:
            self.id = self._get_new_game_instance()

    def add_player(self, name, player_no):
        request = self.__message_handler. \
            create_request('add_player', self.id, player_name=name, player_number=player_no)
        return self.controller.get(**request)

    def get_current_player(self):
        request = self.__message_handler.create_request('get_current_player', self.id)
        return self.controller.get(**request)

    def get_board(self):
        request = self.__message_handler.create_request('get_board', self.id)
        return self.controller.get(**request)

    def make_move(self, field):
        request = self.__message_handler.create_request('make_move', self.id, chosen_field=field)
        return self.controller.get(**request)

    def _get_new_game_instance(self):
        request = self.__message_handler.create_request('get_new_game_instance', 0, mode=self.__game_mode_multiplayer)
        return self.controller.get(**request)

    def check_game_result(self):
        request = self.__message_handler.create_request('check_game_result', self.id)
        result = self.controller.get(**request)
        return result if result != 'False' else None

    def end_game(self):
        request = self.__message_handler.create_request('end_game', self.id)
        self.controller.get(**request)

    def play(self):
        try:
            self._init_players()
            result = None
            while not result:
                result = self._perform_next_move()
            self._finish_game(result)
        except EOFError:
            print('Quitting the game...')

    def _init_players(self):
        player1 = input('Please enter yor name (Player 1)\n')
        self.add_player(player1, 0)

        player2 = input('Please enter yor name (Player 2)\n')
        self.add_player(player2, 1)

    def _perform_next_move(self):
        print(self.get_board())
        move_ok = None
        while not move_ok:
            move = input('Player ' + self.get_current_player() + ' enter next move\n')
            move_ok = self.make_move(move)
        return self.check_game_result()

    def _finish_game(self, result):
        print('Game Over!')
        print(self.get_board())
        print(result)
        self.end_game()
        print('Thank you.')


if __name__ == '__main__':
    game = OXGame()
    game.play()