import json_creator


class Message:
    def __init__(self):
        self.sent_from = ''
        self.text = ''
        self.sent_to = ''
        self._builder = json_creator.MessageBuilder

    def read(self):
        pass

    def get_message(self):
        return self._builder.get_message(self.sent_from,
                                         self.sent_to,
                                         self.text)


class Chat:
    def __init__(self):
        self.clients = []
        self.messages = []
