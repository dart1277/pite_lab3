from game.server.controller import Controller
import unittest
from unittest.mock import patch


class TestOxController(unittest.TestCase):

    @patch('game.server.config.OXModel')
    @patch('game.server.config.OXView')
    def test_controller_add_player(self, console_view_mock, model_mock):
        con = Controller()
        model_mock.return_value = model_mock
        model_mock.add_player.return_value = True  # Model's method must return sthg other than None, 0, False
        console_view_mock.add_player.return_value = None  # unless we want the Controller to Call OXConsoleView.error

        g_id = con.get('get_new_game_instance_ox', '0', 'True')
        out = con.get('add_player_ox', str(g_id), 'name1', '0')

        self.assertEqual(out, None)  # console_view_mock.add_player.return_value == None
        model_mock.add_player.assert_called_with(model_mock, 'name1', '0')
        console_view_mock.add_player.assert_called_with(console_view_mock, model_mock, True)

    @patch('game.server.config.OXModel')
    @patch('game.server.config.OXView')
    def test_controller_get_current_player(self, console_view_mock, model_mock):
        con = Controller()
        model_mock.return_value = model_mock
        model_mock.get_current_player.return_value = True
        console_view_mock.get_current_player.return_value = None

        g_id = con.get('get_new_game_instance_ox', '0', 'True')
        out = con.get('get_current_player_ox', str(g_id), 'name1', '0')

        self.assertEqual(out, None)
        model_mock.get_current_player.assert_called_with(model_mock, 'name1', '0')
        console_view_mock.get_current_player.assert_called_with(console_view_mock, model_mock, True)

    @patch('game.server.config.OXModel')
    @patch('game.server.config.OXView')
    def test_controller_get_board(self, console_view_mock, model_mock):
        con = Controller()
        model_mock.return_value = model_mock
        model_mock.get_board.return_value = True
        console_view_mock.get_board.return_value = None

        g_id = con.get('get_new_game_instance_ox', '0', 'True')
        out = con.get('get_board_ox', str(g_id), 'name1', '0')

        self.assertEqual(out, None)
        model_mock.get_board.assert_called_with(model_mock, 'name1', '0')
        console_view_mock.get_board.assert_called_with(console_view_mock, model_mock, True)

    @patch('game.server.config.OXModel')
    @patch('game.server.config.OXView')
    def test_controller_make_move(self, console_view_mock, model_mock):
        con = Controller()
        model_mock.return_value = model_mock
        model_mock.make_move.return_value = True
        console_view_mock.make_move.return_value = None

        g_id = con.get('get_new_game_instance_ox', '0', 'True')
        out = con.get('make_move_ox', str(g_id), 'name1', '0')

        self.assertEqual(out, None)
        model_mock.make_move.assert_called_with(model_mock, 'name1', '0')
        console_view_mock.make_move.assert_called_with(console_view_mock, model_mock, True)

    @patch('game.server.config.OXModel')
    def test_controller_get_new_game_instance(self, model_mock):
        con = Controller()
        old_guid = con._Controller__game_guid
        model_mock.return_value = model_mock
        model_mock.get_new_game_instance.return_value = True
        g_id = con.get('get_new_game_instance_ox', '0', 'True')

        self.assertEqual(old_guid + 1, g_id)

        model_mock.assert_called_with('0', 'True')

    @patch('game.server.config.OXModel')
    def test_controller_get_new_game_instance_too_many_games(self, model_mock):
        con = Controller()
        con._Controller__games = {0: '', 1: ''}
        model_mock.return_value = model_mock
        model_mock.get_new_game_instance.return_value = True
        self.assertRaises(OverflowError, con.get('get_new_game_instance_ox', 0))

    @patch('game.server.config.OXModel')
    @patch('game.server.config.OXView')
    def test_controller_check_game_result(self, console_view_mock, model_mock):
        con = Controller()
        model_mock.return_value = model_mock
        model_mock.check_game_result.return_value = True
        console_view_mock.check_game_result.return_value = None

        g_id = con.get('get_new_game_instance_ox', '0', 'True')
        out = con.get('check_game_result_ox', str(g_id), 'name1', '0')

        self.assertEqual(out, None)
        model_mock.check_game_result.assert_called_with(model_mock, 'name1', '0')
        console_view_mock.check_game_result.assert_called_with(console_view_mock, model_mock, True)

    def test_controller_end_game(self):
        con = Controller()

        g_id = con.get('get_new_game_instance_ox', '0', 'True')
        out = con.get('end_game_ox', str(g_id), 'name1', '0')

        self.assertEqual(out, None)

    @patch('game.server.config.OXModel')
    @patch('game.server.config.OXView')
    def test_controller_add_player_error(self, console_view_mock, model_mock):
        con = Controller()
        model_mock.return_value = model_mock
        model_mock.add_player.return_value = False  # Model's method must return sthg other than None, 0, False

        g_id = con.get('get_new_game_instance_ox', '0', 'True')
        con.get('add_player_ox', str(g_id), 'name1', '0')

        model_mock.add_player.assert_called_with(model_mock, 'name1', '0')
        console_view_mock.error.assert_called_with(console_view_mock, model_mock, False)

    @patch('game.server.config.OXModel')
    @patch('game.server.config.OXView')
    def test_controller_get_current_player_error(self, console_view_mock, model_mock):
        con = Controller()
        model_mock.return_value = model_mock
        model_mock.get_current_player.return_value = False

        g_id = con.get('get_new_game_instance_ox', '0', 'True')
        con.get('get_current_player_ox', str(g_id), 'name1', '0')

        model_mock.get_current_player.assert_called_with(model_mock, 'name1', '0')
        console_view_mock.error.assert_called_with(console_view_mock, model_mock, False)

    @patch('game.server.config.OXModel')
    @patch('game.server.config.OXView')
    def test_controller_get_board_error(self, console_view_mock, model_mock):
        con = Controller()
        model_mock.return_value = model_mock
        model_mock.get_board.return_value = False

        g_id = con.get('get_new_game_instance_ox', '0', 'True')
        con.get('get_board_ox', str(g_id), 'name1', '0')

        model_mock.get_board.assert_called_with(model_mock, 'name1', '0')
        console_view_mock.error.assert_called_with(console_view_mock, model_mock, False)

    @patch('game.server.config.OXModel')
    @patch('game.server.config.OXView')
    def test_controller_make_move_error(self, console_view_mock, model_mock):
        con = Controller()
        model_mock.return_value = model_mock
        model_mock.make_move.return_value = False

        g_id = con.get('get_new_game_instance_ox', '0', 'True')
        con.get('make_move_ox', str(g_id), 'name1', '0')

        model_mock.make_move.assert_called_with(model_mock, 'name1', '0')
        console_view_mock.error.assert_called_with(console_view_mock, model_mock, False)

    @patch('game.server.config.OXModel')
    @patch('game.server.config.OXView')
    def test_controller_check_game_result_error(self, console_view_mock, model_mock):
        con = Controller()
        model_mock.return_value = model_mock
        model_mock.check_game_result.return_value = False

        g_id = con.get('get_new_game_instance_ox', '0', 'True')
        con.get('check_game_result_ox', str(g_id), 'name1', '0')

        model_mock.check_game_result.assert_called_with(model_mock, 'name1', '0')
        console_view_mock.error.assert_called_with(console_view_mock, model_mock, False)


if __name__ == '__main__':
    unittest.main()
