import logging
import logging.handlers
from functools import wraps

logging.basicConfig(
    format="%(asctime)s %(levelno)-5s %(module)-15s %(funcName)-20s %(message)s",
    level=logging.INFO
)

logger = logging.getLogger('app.' + __name__)

server_log_filename = 'server.log'
server_handler = logging.FileHandler(server_log_filename)
server_handler = logging.handlers.TimedRotatingFileHandler(
    filename=server_log_filename,
    when='D',
    interval=1)

client_log_filename = 'client.log'
client_handler = logging.FileHandler(client_log_filename)

test_log_filename = 'test.log'
test_handler = logging.FileHandler(test_log_filename)


class Log:
    def __init__(self, log_type):
        if log_type == 'client':
            self.logger = logging.getLogger('dwt.server')
            self.logger.addHandler(server_handler)
        elif log_type == 'server':
            self.logger = logging.getLogger('dwt.client')
            self.logger.addHandler(client_handler)
        elif log_type == 'test':
            self.logger = logging.getLogger('dwt.test')
            self.logger.addHandler(test_handler)

    def __call__(self, function):
        """
        Decorates function with logging. Logs its name and arguments at INFO level.
        :param function: Function to decorate
        :type function: Function
        :return: Decorated function
        :rtype: Function's return
        """

        @wraps(function)
        def inner_function(*args, **kwargs):
            log_params = {'func_name': function.__name__, 'args': str(args),
                          'kwargs': str(kwargs)}
            self.logger.info("Function: {func_name}, Arguments: {args}, "
                             "Keyword Arguments: {kwargs}".format(
                **log_params))
            return function(*args, **kwargs)

        return inner_function
