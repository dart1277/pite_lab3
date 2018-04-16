from game.server.views import OXView, IntervalView
from game.server.models import OXModel, IntervalModel


class ViewResolver:

    @staticmethod
    def resolve(action, config):
        if action.endswith('ox'):
            return config.view_ox
        if action.endswith('interval'):
            return config.view_interval


class Config:
    def __init__(self):
        self.model_ox = OXModel
        self.view_ox = OXView
        self.view_interval = IntervalView
        self.model_interval = IntervalModel
        self.actions = {'add_player_ox': {'model': self.model_ox.add_player,
                                          'view': self.view_ox.add_player,
                                          'error_view': self.view_ox.error
                                          },
                        'get_current_player_ox': {'model': self.model_ox.get_current_player,
                                                  'view': self.view_ox.get_current_player,
                                                  'error_view': self.view_ox.error
                                                  },
                        'get_board_ox': {'model': self.model_ox.get_board,
                                         'view': self.view_ox.get_board,
                                         'error_view': self.view_ox.error
                                         },
                        'make_move_ox': {'model': self.model_ox.make_move,
                                         'view': self.view_ox.make_move,
                                         'error_view': self.view_ox.error
                                         },
                        'get_new_game_instance_ox': {'model': self.model_ox,
                                                     'view': None,
                                                     'error_view': None
                                                     },
                        'check_game_result_ox': {'model': self.model_ox.check_game_result,
                                                 'view': self.view_ox.check_game_result,
                                                 'error_view': self.view_ox.error
                                                 },
                        'end_game_ox': {'model': None, 'view': None, 'error_view': None},

                        'add_player_interval': {'model': self.model_interval.add_player,
                                                'view': self.view_interval.add_player,
                                                'error_view': self.view_interval.error
                                                },
                        'get_current_player_interval': {'model': self.model_interval.get_current_player,
                                                        'view': self.view_interval.get_current_player,
                                                        'error_view': self.view_interval.error
                                                        },
                        'get_board_interval': {'model': self.model_interval.get_board,
                                               'view': self.view_interval.get_board,
                                               'error_view': self.view_interval.get_board
                                               },
                        'make_move_interval': {'model': self.model_interval.make_move,
                                               'view': self.view_interval.make_move,
                                               'error_view': self.view_interval.error
                                               },
                        'get_new_game_instance_interval': {'model': self.model_interval,
                                                           'view': None,
                                                           'error_view': None
                                                           },
                        'check_game_result_interval': {'model': self.model_interval.check_game_result,
                                                       'view': self.view_interval.check_game_result,
                                                       'error_view': self.view_interval.error
                                                       },
                        'end_game_interval': {'model': None, 'view': None, 'error_view': None}
                        }
