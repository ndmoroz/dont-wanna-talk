# Tests for client
import socket
import unittest
from server import Server
import client
from threading import Thread


class TestGetServerIpPort(unittest.TestCase):
    def test_no_args(self):
        arguments = ['client.py']
        function_ip, function_port = client.get_server_ip_port(arguments)
        self.assertIsNone(function_ip)

    def test_only_ip(self):
        correct_ip = '0.0.0.0'
        correct_port = 7777
        arguments = ['client.py', correct_ip]
        self.assertEqual((correct_ip, correct_port),
                         client.get_server_ip_port(arguments))

    def test_ip_and_port(self):
        correct_ip = '0.0.0.0'
        correct_port = 1234
        arguments = ['client.py', correct_ip, str(correct_port)]
        self.assertEqual((correct_ip, correct_port),
                         client.get_server_ip_port(arguments))


class TestGetClientSocket(unittest.TestCase):
    def test_correct_ip_port(self):
        server_ip = '127.0.0.1'
        server_port = 7777
        server = Server()
        p = Thread(target=server.main)
        p.start()
        function_socket = client.get_client_socket(server_ip, server_port)
        self.assertEqual((server_ip, server_port),
                         function_socket.getpeername())
        server.stop()


if __name__ == '__main__':
    unittest.main()
