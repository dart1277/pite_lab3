class Validator:
    max_field_length = 30

    @staticmethod
    def can_add_player(name, player_id, players_count):
        return (player_id is not None and players_count > player_id >= 0 and
                name and any(c.isalpha() for c in name.strip()) and
                len(name) < Validator.max_field_length)

    @staticmethod
    def str_to_int(val):
        try:
            val = int(val)
            return val
        except ValueError:
            return
