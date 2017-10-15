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
