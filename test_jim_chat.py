import unittest
import jim_chat
import json_creator
from common_functions import are_equal_dicts


class TestParseMessage(unittest.TestCase):
    def test_parse_message(self):
        msg = jim_chat.Message()
        text = 'I don\'t really wanna talk'
        username = 'Alice'
        to = 'Bob'
        message_to_read = json_creator.get_message(to, username, text)
        msg.parse_message(message_to_read)
        self.assertEqual(text, msg.text)
        self.assertEqual(username, msg.sent_from)
        self.assertEqual(to, msg.sent_to)


class TestGetMessage(unittest.TestCase):
    def test_get_message(self):
        msg = jim_chat.Message()
        msg.sent_to = 'Bob'
        msg.sent_from = 'Alice'
        msg.text = 'I don\'t really wanna talk'
        object_message = msg.get_message()
        correct_message = {'action': 'msg', 'time': 0,
                           'to': 'Bob', 'from': 'Alice',
                           'encoding': 'utf-8',
                           'message': 'I don\'t really wanna talk'}
        self.assertTrue(
            are_equal_dicts(correct_message, object_message, 'time'))
