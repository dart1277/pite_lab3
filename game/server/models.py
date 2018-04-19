import math
import random
from game.server.models_validator import Validator


class GameModel:
    def __init__(self, game_id, game_mode_multiplayer):
        self._id = game_id
        self._players = ['Player 1', 'Player 2']
        self._game_mode = game_mode_multiplayer == 'True'
        if not self._game_mode:
            self._players[1] = 'Computer'
        self._current_player = 0

    def add_player(self, name, player_id):
        player_id = self._str_to_int(player_id)
        if self._can_add_player(name, player_id):
            self._players[player_id] = str(name)
            return True

    def _can_add_player(self, name, player_id):
        valid = Validator.can_add_player(name, player_id, self.get_players_count())
        return valid if self._game_mode else valid and player_id == 0  # for single player mode player 0 is valid

    def _str_to_int(self, val):
        return Validator.str_to_int(val)

    def _switch_player(self):
        pass

    def get_players_count(self):
        return len(self._players)

    def get_current_player(self):
        return self._players[self._current_player]

    def get_current_player_number(self):
        return self._current_player


class OXModel(GameModel):
    def __init__(self, game_id, game_mode_multiplayer):
        super().__init__(game_id, game_mode_multiplayer)
        self.__board_len = 9
        self._board = [-1 for it in range(0, self.__board_len)]

    def get_board(self):
        return self._board[:]

    def __is_move_valid(self, field):
        if self._is_field_on_board(field) and self._is_field_untouched(field):
            return True

    def _is_field_on_board(self, field):
        return 0 <= field < len(self._board)

    def _is_field_untouched(self, field):
        return self._board[field] == -1

    def make_move(self, field):
        field = self._str_to_int(field)
        if self._can_make_a_move(field):
            self._board[field] = self._current_player
            self._switch_player()
            return True
        return False

    def _switch_player(self):
        if self._game_mode:
            self._current_player = (self._current_player + 1) % len(self._players)
        else:
            free_fields = [u for u, v in enumerate(self._board) if v == -1]
            computer_move_ok = self.check_game_result() == 'False'
            if free_fields and computer_move_ok:
                computer_move = random.choice(free_fields)
                self._board[computer_move] = len(self._players) - 1

    def _can_make_a_move(self, field):
        return field is not None and self.__is_move_valid(field)

    def check_game_result(self):
        dim = int(math.sqrt(self.__board_len))
        result = None

        class FoundException(Exception):
            pass

        def row():
            return self._board[i * dim: i * dim + dim]

        def col():
            return [self._board[j * dim + i] for j in range(0, dim)]

        def diag():
            return [self._board[j * dim + j] for j in range(0, dim)]

        def diag2():
            return [self._board[j * dim + dim - j - 1] for j in range(0, dim)]

        def check_slice(sli):
            if _is_slice_filled_for_one_player(sli):
                raise FoundException(self._players[min(sli)])  # winner = min, because he is starting

        def _is_slice_filled_for_one_player(sli):
            return max(sli) == min(sli) != -1

        def _is_game_out_of_moves():
            return all(map(lambda x: x != -1, self._board))

        try:
            for i in range(0, dim):
                check_slice(row())
                check_slice(col())
            check_slice(diag())
            check_slice(diag2())
            if _is_game_out_of_moves():
                result = 'A draw'
        except FoundException as e:
            result = str(e) + ' won the game!'
        return result if result is not None else 'False'


class IntervalModel(GameModel):

    def __init__(self, game_id, game_mode_multiplayer):
        super().__init__(game_id, 'False')
        self.__upper_limit = 100
        self.__lower_limit = 0
        self.__random_secret = random.randrange(self.__lower_limit, self.__upper_limit)
        self.__last_guess = self.__lower_limit - 1
        self.__guesses = []

    def get_board(self):
        return self.__guesses

    def get_random_secret(self):
        return self.__random_secret

    def get_last_guess(self):
        return self.__last_guess

    def get_lower_limit(self):
        return self.__lower_limit

    def get_upper_limit(self):
        return self.__upper_limit

    def make_move(self, value):
        field = self._str_to_int(value)
        if self._is_move_valid(field):
            self.__last_guess = field
            return True
        return False

    def _is_move_valid(self, field):
        return self.__lower_limit <= field <= self.__upper_limit and field not in self.__guesses

    def check_game_result(self):
        if self.__last_guess < self.__lower_limit:
            raise ValueError('check_game_result called before first move')
        self.__guesses.append(self.__last_guess)
        self.__guesses.sort()
        return self._game_result()

    def _game_result(self):
        current_moves_count = len(self.__guesses)
        margin = 3
        player = 'False'
        if current_moves_count > math.log2(self.__upper_limit - self.__lower_limit + 1) + margin:
            player = self._players[1] + ' won the game :('
        elif self.__last_guess == self.__random_secret:
            player = self._players[0] + ' won the game !!'
        return player
