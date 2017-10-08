# Tests for json_creator
import json_creator
import unittest
import time


def are_equal_dicts(dict1, dict2, *ignore_keys):
    d1_filtered = dict(
        (k, v) for k, v in dict1.items() if k not in ignore_keys)
    d2_filtered = dict(
        (k, v) for k, v in dict2.items() if k not in ignore_keys)
    return d1_filtered == d2_filtered


class TestGetPresenceJson(unittest.TestCase):
    def test_presence_json(self):
        correct_message = {'action': 'presence',
                           'time': 0,
                           'type': 'status',
                           'user':
                               {'account_name': 'M', 'status': 'Here'}}
        function_message = json_creator.get_presence_json('M', 'Here')
        self.assertTrue(
            are_equal_dicts(correct_message, function_message, 'time'))


class TestGetProbeJson(unittest.TestCase):
    def test_probe_json(self):
        correct_message = {'action': 'probe',
                           'time': time.time()}
        function_message = json_creator.get_probe_json()
        self.assertTrue(
            are_equal_dicts(correct_message, function_message, 'time'))


class TestGetEmptyResponse(unittest.TestCase):
    def test_ok_response(self):
        correct_message = {'response': 'ok'}
        function_message = json_creator.get_empty_response_json('ok')
        self.assertTrue(are_equal_dicts(correct_message, function_message))

    def test_wrong_type_response(self):
        with self.assertRaises(TypeError):
            function_message = json_creator.get_empty_response_json(None, None)


class TestIsLongName(unittest.TestCase):
    def test_long_name(self):
        self.assertTrue(json_creator.is_long_name('a' * 26))

    def test_short_name(self):
        self.assertFalse(json_creator.is_long_name('a' * 25))


class TestGetAutenticateMessage(unittest.TestCase):
    def test_normal_case(self):
        correct_message = {'action': 'authenticate', 'time': time.time(),
                           'user':
                               {'account_name': 'M', 'password': '123'}}
        function_message = json_creator.get_authenticate_json('M', '123')
        self.assertTrue(
            are_equal_dicts(correct_message, function_message, 'time'))

    def test_no_pass_case(self):
        correct_message = {'action': 'authenticate', 'time': time.time(),
                           'user':
                               {'account_name': 'M', 'password': ''}}
        function_message = json_creator.get_authenticate_json('M', '')
        self.assertTrue(
            are_equal_dicts(correct_message, function_message, 'time'))

    def test_long_name(self):
        function_message = json_creator.get_authenticate_json(
            'abcdefghijklmnopqrstuvwxyz', '123')
        self.assertIsNone(function_message)


class TestGetChatroomMessage(unittest.TestCase):
    def test_normal_case(self):
        correct_message = {'action': 'msg', 'time': time.time(),
                           'to': 'MainChat', 'from': 'Alice',
                           'message': 'I don\'t really wanna talk'}
        function_message = \
            json_creator.get_chatroom_message('MainChat', 'Alice',
                                              'I don\'t really wanna talk')
        self.assertTrue(
            are_equal_dicts(correct_message, function_message, 'time'))


if __name__ == '__main__':
    unittest.main()
