from unittest import TestCase

from game.server.models import OXModel


class TestOXModel(TestCase):
    testModel = None
    test_name = 'testName'
    player1 = 'Player 1'
    player2 = 'Player 2'

    def setUp(self):
        super().setUp()
        self.testModel = OXModel(0, 'True')

    def test_add_player(self):
        test_id = 0

        self.testModel.add_player(self.test_name, test_id)

        self.assertEqual(self.test_name, self.testModel._players[test_id])
        self.assertEqual(self.player2, self.testModel._players[1])

    def test_add_player_id_len_too_big(self):
        test_id = 4

        self.testModel.add_player(self.test_name, test_id)

        self.assertEqual(self.player1, self.testModel._players[0])
        self.assertEqual(self.player2, self.testModel._players[1])

    def test_add_player_id_negative(self):
        test_id = -3

        self.testModel.add_player(self.test_name, test_id)

        self.assertEqual(self.player1, self.testModel._players[0])
        self.assertEqual(self.player2, self.testModel._players[1])

    def test_get_players_count(self):
        expected_count = 2

        result_count = self.testModel.get_players_count()

        self.assertEqual(expected_count, result_count)

    def test_get_current_player_zero(self):
        result_player = self.testModel.get_current_player()

        self.assertEqual(self.player1, result_player)

    def test_get_current_player_one(self):
        self.testModel._current_player = 1

        result_player = self.testModel.get_current_player()

        self.assertEqual(self.player2, result_player)

    def test_get_board(self):
        expected_board_len = 9
        expected_board = [-1 for it in range(0, expected_board_len)]

        result_board = self.testModel.get_board()

        self.assertEqual(expected_board, result_board)
        self.assertEqual(expected_board_len, len(result_board))

    def test_make_move(self):
        board_len = 9
        board = [-1 for it in range(0, board_len)]
        field_to_move = 3

        expected = self.testModel.make_move(field_to_move)
        result_board = self.testModel._board
        result_player = self.testModel._current_player

        self.assertTrue(expected)
        self.assertNotEqual(board, result_board)
        self.assertNotEqual(self.player1, result_player)

    def test_make_move_invalid_argument(self):
        invalid_argument = 'invalid'

        expected = self.testModel.make_move(invalid_argument)

        self.assertFalse(expected)

    def test_check_game_result_ingame(self):
        result = self.testModel.check_game_result()

        self.assertEqual('False', result)

    def test_check_game_result_win(self):
        expected_result = self.player1 + ' won the game!'
        board_len = 9
        self.testModel._board = [0 for it in range(0, board_len)]

        result = self.testModel.check_game_result()

        self.assertEqual(expected_result, result)

    def test_check_game_result_draw(self):
        expected_result = 'A draw'
        self.testModel._board = [1, 1, 0, 0, 1, 1, 1, 0, 0]

        result = self.testModel.check_game_result()

        self.assertEqual(expected_result, result)
