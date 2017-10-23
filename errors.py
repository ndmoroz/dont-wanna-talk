class NotMessageError(Exception):
    def __init__(self, not_message):
        self.message = not_message

    def __str__(self):
        return 'Not a message: {}'.format(self.mode)


class LongUsernameError(Exception):
    def __init__(self, username):
        self.username = username

    def __str__(self):
        return 'Name {} is too long: {} symbols, maximum allowed is 25'.format(
            self.username, len(self.username))


class WrongResponseCodeError(Exception):
    def __init__(self, code):
        self.code = code

    def __str__(self):
        return 'Wrong response code: {}'.format(self.code)


class UnknownMessageFormatError(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return 'Unknown type of message: {}'.format(self.message)
