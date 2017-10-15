import unittest
import jim_chat
from time import time


class TestGetMessage(unittest.TestCase):
    def test_read_json(self):
        msg = jim_chat.Message
        text = 'I don\'t really wanna talk'
        username = 'Alice'
        to = 'MainChat'

        message_to_read = {'action': 'msg', 'time': time(),
                           'to': to, 'from': username,
                           'message': text}

        msg.read_json(message_to_read)

        self.assertEqual(text, msg.text)
        self.assertEqual(username, msg.username)
        self.assertEqual(to, msg.to)
