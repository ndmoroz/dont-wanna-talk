import json_creator


class Message:
    def __init__(self, sent_to, sent_from, text):
        self.sent_from = sent_from
        self.text = text
        self.sent_to = sent_to

    def parse_message(self, message_dict):
        self.sent_from = json_creator.get_message_sendfrom(message_dict)
        self.sent_to = json_creator.get_message_sendto(message_dict)
        self.text = json_creator.get_message_text(message_dict)

    def get_message(self):
        return json_creator.get_message(self.sent_to, self.sent_from,
                                        self.text)


class Chat:
    def __init__(self):
        self.clients = []
        self.messages = []

    def add_client(self, user):
        self.clients.append(user)

    def remove_client(self, user):
        self.clients.remove(user)


class Client:
    def __init__(self):
        self.chat = []
        self.username = ''

    def set_username(self, username):
        self.username = username

    def send_message(self, sendto, message):
        new_message = Message(sendto, self.username, message)
