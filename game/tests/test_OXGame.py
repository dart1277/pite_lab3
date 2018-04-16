from unittest import TestCase
from unittest.mock import patch

from game.client.console import OXGame


class TestOXGame(TestCase):
    @patch('game.client.console.OXGame.prompt_user_for_game_type', return_value=('ox', False))
    @patch('game.client.OXControllerNetworkClient.OXControllerNetworkClient.get')
    def test_add_player(self, controller_mock, game_sel):
        game = OXGame()
        game.id = 1

        game.add_player("test", 0)

        controller_mock.assert_called_with(
            '[["method", "add_player_ox"], ["id", "1"], ["player_name", "test"], ["player_number", "0"]]')

    @patch('game.client.console.OXGame.prompt_user_for_game_type', return_value=('ox', False))
    @patch('game.client.OXControllerNetworkClient.OXControllerNetworkClient.get')
    def test_get_current_player(self, controller_mock, game_sel):
        game = OXGame()
        game.id = 1

        game.get_current_player()

        controller_mock.assert_called_with('[["method", "get_current_player_ox"], ["id", "1"]]')

    @patch('game.client.console.OXGame.prompt_user_for_game_type', return_value=('ox', False))
    @patch('game.client.OXControllerNetworkClient.OXControllerNetworkClient.get')
    def test_get_board(self, controller_mock, game_sel):
        game = OXGame()

        game.id = 1

        game.get_board()

        controller_mock.assert_called_with('[["method", "get_board_ox"], ["id", "1"]]')

    @patch('game.client.console.OXGame.prompt_user_for_game_type', return_value=('ox', False))
    @patch('game.client.OXControllerNetworkClient.OXControllerNetworkClient.get')
    def test_make_move(self, controller_mock, game_sel):
        game = OXGame()

        game.id = 1

        game.make_move(3)

        controller_mock.assert_called_with('[["method", "make_move_ox"], ["id", "1"], ["chosen_field", "3"]]')

    @patch('game.client.console.OXGame.prompt_user_for_game_type', return_value=('ox', True))
    @patch('game.client.OXControllerNetworkClient.OXControllerNetworkClient.get')
    def test__get_new_game_instance(self, controller_mock, game_sel):
        game = OXGame()

        game._get_new_game_instance()

        controller_mock.assert_called_with('[["method", "get_new_game_instance_ox"], ["id", "0"], ["mode", "True"]]')

    @patch('game.client.console.OXGame.prompt_user_for_game_type', return_value=('ox', False))
    @patch('game.client.OXControllerNetworkClient.OXControllerNetworkClient.get')
    def test_check_game_result_true(self, controller_mock, game_sel):
        controller_mock.return_value = True
        game = OXGame()

        game.id = 1

        result = game.check_game_result()

        self.assertEqual(True, result)
        controller_mock.assert_called_with('[["method", "check_game_result_ox"], ["id", "1"]]')

    @patch('game.client.console.OXGame.prompt_user_for_game_type', return_value=('ox', False))
    @patch('game.client.OXControllerNetworkClient.OXControllerNetworkClient.get')
    def test_check_game_result_none(self, controller_mock, game_sel):
        controller_mock.return_value = 'False'
        game = OXGame()

        game.id = 1

        result = game.check_game_result()

        self.assertEqual(None, result)
        controller_mock.assert_called_with('[["method", "check_game_result_ox"], ["id", "1"]]')

    @patch('game.client.console.OXGame.prompt_user_for_game_type', return_value=('ox', False))
    @patch('game.client.OXControllerNetworkClient.OXControllerNetworkClient.get')
    def test_end_game(self, controller_mock, game_sel):
        game = OXGame()

        game.id = 1

        game.end_game()

        controller_mock.assert_called_with('[["method", "end_game_ox"], ["id", "1"]]')

    @patch('game.client.console.OXGame.prompt_user_for_game_type', return_value=('ox', False))
    @patch('game.client.OXControllerNetworkClient.OXControllerNetworkClient.get')
    def test_play(self, controller_mock, game_sel):
        controller_mock.return_value = 'True'
        game = OXGame()

        game.id = 1

        with patch('builtins.input', return_value=1):
            game.play()

        controller_mock.assert_called_with('[["method", "end_game_ox"], ["id", "1"]]')

    @patch('game.client.console.OXGame.prompt_user_for_game_type', return_value=('ox', False))
    @patch('game.client.OXControllerNetworkClient.OXControllerNetworkClient.get')
    def test__init_players(self, controller_mock, game_sel):
        game = OXGame()

        game.id = 1

        with patch('builtins.input', return_value='test'):
            game.init_players()

        controller_mock.assert_called_with(
            '[["method", "add_player_ox"], ["id", "1"], ["player_name", "test"], ["player_number", "0"]]')

    @patch('game.client.console.OXGame.prompt_user_for_game_type', return_value=('ox', False))
    @patch('game.client.OXControllerNetworkClient.OXControllerNetworkClient.get')
    def test__perform_next_move(self, controller_mock, game_sel):
        controller_mock.return_value = 'True'
        game = OXGame()

        game.id = 1

        with patch('builtins.input', return_value=1):
            game.perform_next_move()

        controller_mock.assert_called_with(
            '[["method", "check_game_result_ox"], ["id", "1"]]')

    @patch('game.client.console.OXGame.prompt_user_for_game_type', return_value=('ox', False))
    @patch('game.client.OXControllerNetworkClient.OXControllerNetworkClient.get')
    def test__finish_game(self, controller_mock, game_sel):
        game = OXGame()

        game.id = 1
        game._in_game_result = "test"

        game.finish_game()

        controller_mock.assert_called_with(
            '[["method", "end_game_ox"], ["id", "1"]]')
