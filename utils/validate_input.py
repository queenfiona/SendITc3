"""Docstring for validate_input.py."""


class CheckUserInput(object):
    """docstring for CheckUserInput."""

    def check_if_input_is_string(self, user_input):
        """Docstring for validating if input is str."""
        if type(user_input) is not str:
            return False
        elif bool(user_input.strip()) is False:
            return False
        elif self.check_if_input_is_integer(user_input) is True:
            return False
        else:
            return True

    def check_if_input_is_integer(self, user_input):
        """Docstring for validating if input is int."""
        try:
            int(user_input)
        except ValueError:
            return False
        else:
            if int(user_input) > 0:
                return True
