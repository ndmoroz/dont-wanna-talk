# Tests for client
import socket
import unittest
from server import Server
import client
from threading import Thread
import subprocess
from time import sleep

# class TestGetServerIpPort(unittest.TestCase):
#     def test_no_args(self):
#         arguments = ['client.py']
#         function_ip, function_port = client.get_server_ip_port(arguments)
#         self.assertIsNone(function_ip)
#
#     def test_only_ip(self):
#         correct_ip = '0.0.0.0'
#         correct_port = 7777
#         arguments = ['client.py', correct_ip]
#         self.assertEqual((correct_ip, correct_port),
#                          client.get_server_ip_port(arguments))
#
#     def test_ip_and_port(self):
#         correct_ip = '0.0.0.0'
#         correct_port = 1234
#         arguments = ['client.py', correct_ip, str(correct_port)]
#         self.assertEqual((correct_ip, correct_port),
#                          client.get_server_ip_port(arguments))
#
#
# class TestGetClientSocket(unittest.TestCase):
#     def test_correct_ip_port(self):
#         server_ip = '127.0.0.1'
#         server_port = 7777
#         server = Server()
#         p = Thread(target=server.main)
#         p.start()
#         function_socket = client.get_client_socket(server_ip, server_port)
#         self.assertEqual((server_ip, server_port),
#                          function_socket.getpeername())
#         server.stop()

#
# class TestServerClient(unittest.TestCase):
#     def test_reader_gets_writer_message(self):
#         # Launching server, client-writer and client-reader
#         # specifying encoding to communicate in strings, not in bytes
#         server = subprocess.Popen(['python', 'server.py'],
#                                   stdout=subprocess.PIPE,
#                                   stdin=subprocess.PIPE,
#                                   stderr=subprocess.STDOUT,
#                                   encoding='utf-8')
#         writer = subprocess.Popen(['python', 'client.py', '-w', 'localhost'],
#                                   stdout=subprocess.PIPE,
#                                   stdin=subprocess.PIPE,
#                                   stderr=subprocess.STDOUT,
#                                   encoding='utf-8')
#
#
#         print(0)
#         try:
#             print(server.stdout.readline())
#         except:
#             pass
#
#         print(1)
#         try:
#             print(writer.stdout.readline())
#         except:
#             pass
#
#         print(2)
#         try:
#             print(writer.stdout.readline())
#         except:
#             pass
#
#         print(3.0)
#         try:
#             print(writer.stdout.readline())
#         except:
#             pass
#
#         print(3.1)
#         try:
#             writer.stdin.write("writerName\n")
#             writer.stdin.flush()
#         except:
#             pass
#
#         print(3.2)
#         try:
#             print(server.stdout.readline())
#         except:
#             pass
#
#         print(4.1)
#         try:
#             writer.stdin.write("message1\n")
#             writer.stdin.flush()
#         except:
#             pass
#
#         print(4.2)
#         try:
#             print(server.stdout.readline())
#         except:
#             pass
#
#         reader = subprocess.Popen(['python', 'client.py', '-r', 'localhost'],
#                                   stdout=subprocess.PIPE,
#                                   stdin=subprocess.PIPE,
#                                   stderr=subprocess.STDOUT,
#                                   encoding='utf-8')
#
#         print(0)
#         try:
#             print(reader.stdout.readline())
#         except:
#             pass
#
#         print(0)
#         try:
#             print(reader.stdout.readline())
#         except:
#             pass
#
#         print(0)
#         try:
#             print(reader.stdout.readline())
#         except:
#             pass
#
#
#         print(5.0)
#         try:
#             print(server.stdout.readline())
#         except:
#             pass
#
#         print(5.1)
#         try:
#             reader.stdin.write("readerName\n")
#             reader.stdin.flush()
#         except:
#             pass
#
#         print(0)
#         try:
#             print(reader.stdout.readline())
#         except:
#             pass
#
#         print(5.2)
#         try:
#             print(server.stdout.readline())
#         except:
#             pass
#
#         print(6.1)
#         try:
#             writer.stdin.write("message1\n")
#             writer.stdin.flush()
#         except:
#             pass
#
#         print(6.2)
#         try:
#             print(reader.stdout.readline())
#         except:
#             pass
#
#         server.kill()
#         writer.kill()
#         reader.kill()
#
#         has_reader_received = \
#             '"from": "writerName", "message": "message1"}' in reader_output
#         self.assertTrue(has_reader_received)






if __name__ == '__main__':
    unittest.main()
