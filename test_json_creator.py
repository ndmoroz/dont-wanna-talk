# Tests for json_creator
import json_creator
import unittest
import errors
from common_functions import are_equal_dicts


class TestJimField(unittest.TestCase):
    def test_in_operator(self):
        self.assertTrue(
            json_creator.JimField.response in json_creator.JimField())
        self.assertFalse(
            'sometext' in json_creator.JimField())


class TestJimAction(unittest.TestCase):
    def test_in_operator(self):
        self.assertTrue(
            json_creator.JimAction.authenticate in json_creator.JimAction())
        self.assertFalse(
            'sometext' in json_creator.JimAction())


class TestJimCode(unittest.TestCase):
    def test_in_operator(self):
        self.assertTrue(404 in json_creator.JimCode())
        self.assertFalse(9999 in json_creator.JimCode())


class TestPresenceMessage(unittest.TestCase):
    def test_presence_with_status(self):
        correct_message = {'action': 'presence',
                           'time': 0,
                           'type': 'status',
                           'user': {'account_name': 'M',
                                    'status': 'Here'}}
        function_message = json_creator.get_presence_message('M', 'Here')
        self.assertTrue(
            are_equal_dicts(correct_message, function_message, 'time'),
            function_message)

    def test_presence_without_status(self):
        correct_message = {'action': 'presence',
                           'time': 0,
                           'user': {'account_name': 'M'}}
        function_message = json_creator.get_presence_message('M')
        self.assertTrue(
            are_equal_dicts(correct_message, function_message, 'time'),
            function_message)

    def test_long_name(self):
        name = 'M' * 26
        with self.assertRaises(errors.LongUsernameError):
            json_creator.get_presence_message(name)


class TestGetProbe(unittest.TestCase):
    def test_probe(self):
        correct_message = {'action': 'probe',
                           'time': 0}
        function_message = json_creator.get_probe_message()
        self.assertTrue(
            are_equal_dicts(correct_message, function_message, 'time'))


class TestGetResponse(unittest.TestCase):
    def test_response_alert(self):
        correct_message = {'response': 200,
                           'alert': 'Everything is OK'}
        function_message = \
            json_creator.get_response_message(200, alert='Everything is OK')
        self.assertTrue(are_equal_dicts(correct_message, function_message))

    def test_response_error(self):
        correct_message = {'response': 402,
                           'error': 'Wrong password'}
        function_message = \
            json_creator.get_response_message(402, error='Wrong password')
        self.assertTrue(are_equal_dicts(correct_message, function_message))

    def test_response_wrong_code(self):
        with self.assertRaises(errors.WrongResponseCodeError):
            json_creator.get_response_message(12, alert='Everything is OK')


class TestGetAutenticateMessage(unittest.TestCase):
    def test_normal_case(self):
        correct_message = {'action': 'authenticate', 'time': 0,
                           'user':
                               {'account_name': 'M', 'password': '123'}}
        function_message = json_creator.get_authenticate_message('M', '123')
        self.assertTrue(
            are_equal_dicts(correct_message, function_message, 'time'))

    def test_no_pass_case(self):
        correct_message = {'action': 'authenticate', 'time': 0,
                           'user':
                               {'account_name': 'M', 'password': ''}}
        function_message = json_creator.get_authenticate_message('M', '')
        self.assertTrue(
            are_equal_dicts(correct_message, function_message, 'time'))

    def test_long_name(self):
        with self.assertRaises(errors.LongUsernameError):
            json_creator.get_authenticate_message(
                'abcdefghijklmnopqrstuvwxyz', '123')


class TestGetMessage(unittest.TestCase):
    def test_normal_case(self):
        correct_message = {'action': 'msg', 'time': 0,
                           'to': 'MainChat', 'from': 'Alice',
                           'encoding': 'utf-8',
                           'message': 'I don\'t really wanna talk'}
        function_message = \
            json_creator.get_message('MainChat', 'Alice',
                                     'I don\'t really wanna talk')
        self.assertTrue(
            are_equal_dicts(correct_message, function_message, 'time'),
            function_message)

    def test_ascii_encoding(self):
        correct_message = {'action': 'msg', 'time': 0,
                           'to': 'MainChat', 'from': 'Alice',
                           'encoding': 'ascii',
                           'message': 'I don\'t really wanna talk'}
        function_message = \
            json_creator.get_message('MainChat', 'Alice',
                                     'I don\'t really wanna talk', 'ascii')
        self.assertTrue(
            are_equal_dicts(correct_message, function_message, 'time'),
            function_message)


class TestGetQuitMessage(unittest.TestCase):
    def test_probe_json(self):
        correct_message = {'action': 'quit'}
        function_message = json_creator.get_quit_message()
        self.assertTrue(
            are_equal_dicts(correct_message, function_message))


class TestIsLongName(unittest.TestCase):
    def test_long_name(self):
        self.assertTrue(json_creator.is_long_name('a' * 26))

    def test_short_name(self):
        self.assertFalse(json_creator.is_long_name('a' * 25))


if __name__ == '__main__':
    unittest.main()
