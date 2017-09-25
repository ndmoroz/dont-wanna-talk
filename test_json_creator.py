# Tests for json_creator

import json_creator
import json
import unittest
import time


class TestGetActionJson(unittest.TestCase):
    def test_long_name(self):
        json_data = {'action': 'do_this'}
        correct_json = json.dumps(json_data)
        function_json = json_creator.get_action_json('do_this')
        self.assertEqual(correct_json, function_json)


class TestIsLongName(unittest.TestCase):
    def test_long_name(self):
        self.assertTrue(json_creator.is_long_name('a' * 26))

    def test_short_name(self):
        self.assertFalse(json_creator.is_long_name('a' * 25))


class TestGetAutenticateMessage(unittest.TestCase):
    def test_normal_case(self):
        authenticate_data = {'action': 'authenticate', 'time': time.time(),
                             'user':
                                 {'account_name': 'M', 'password': '123'}}
        correct_json = json.dumps(authenticate_data)
        function_json = json_creator.get_authenticate_message('M', '123')
        self.assertEqual(correct_json, function_json)

    def test_no_pass_case(self):
        authenticate_data = {'action': 'authenticate', 'time': time.time(),
                             'user':
                                 {'account_name': 'M', 'password': ''}}
        correct_json = json.dumps(authenticate_data)
        function_json = json_creator.get_authenticate_message('M', '')
        self.assertEqual(correct_json, function_json)

    def test_long_name(self):
        function_json = json_creator.get_authenticate_message(
            'abcdefghijklmnopqrstuvwxyz', '123')
        self.assertIsNone(function_json)


if __name__ == '__main__':
    unittest.main()
