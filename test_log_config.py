# Tests logging functions in log config
import log_config
import unittest
import os
import logging


class TestLog(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        Clears test.log if existed
        """
        if os.path.isfile('test.log'):
            log_file = open('test.log', 'w')
            log_file.close()

    def test_function_name_logged(self):
        log = log_config.Log('test')

        @log
        def abc_test():
            pass

        abc_test()
        if not os.path.isfile('test.log'):
            self.fail('Log file is not created')
        with open('test.log', 'r') as log_file:
            exist_line_function_name = 'Function: abc_test' in log_file.read()
        log_file.close()
        self.assertTrue(exist_line_function_name)

    def test_arguments_logged(self):
        log = log_config.Log('test')

        @log
        def abc_test(string, integer):
            pass

        abc_test('a', 1)
        if not os.path.isfile('test.log'):
            self.fail('Log file is not created')
        with open('test.log', 'r') as log_file:
            exist_line_function_name = \
                'Arguments: (\'a\', 1)' in log_file.read()
        log_file.close()
        self.assertTrue(exist_line_function_name)

    def test_keyword_arguments_logged(self):
        log = log_config.Log('test')

        @log
        def abc_test(string, integer):
            pass

        abc_test(string='a', integer=1)
        if not os.path.isfile('test.log'):
            self.fail('Log file is not created')
        with open('test.log', 'r') as log_file:
            exist_line_function_name = \
                'Keyword Arguments: {\'string\': \'a\', \'integer\': 1}' \
                in log_file.read()
        log_file.close()
        self.assertTrue(exist_line_function_name)


if __name__ == '__main__':
    logging.basicConfig(filename="test.log")
    unittest.main()
