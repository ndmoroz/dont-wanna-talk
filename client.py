# Client program
from socket import socket, AF_INET, SOCK_STREAM
from json_creator import json, get_presence_message, get_message
import sys
import log_config
import argparse

log = log_config.Log('client')


class Client:
    def __init__(self):
        pass

    @log
    def parse_arguments(self):
        arg_parser = argparse.ArgumentParser()
        arg_parser.add_argument('-r', action='count')
        arg_parser.add_argument('-w', action='count')
        arg_parser.add_argument('ip')
        arg_parser.add_argument('port', nargs='?', default=7777)
        arguments = arg_parser.parse_args()
        print(arguments)
        self.server_ip = str(arguments.ip)
        self.server_port = int(arguments.port)
        self.rw_status = 'r' if arguments.w is None else 'w'

    @log
    def get_client_socket(self):
        client_socket = socket(AF_INET, SOCK_STREAM)
        client_socket.connect((self.server_ip, self.server_port))
        return client_socket

    @log
    def send_message(self, message):
        self.socket.send(message.encode('utf-8'))

    @log
    def receive_server_response(self):
        return self.socket.recv(1024).decode("utf-8")

    @log
    def start_writer_mode(self):
        while True:
            message = input('Your message ("\\\\\\" to exit): ')
            if message == '\\\\\\':
                break
            self.send_message(
                json(get_message(send_to='Agora',
                                 send_from=self.user_name,
                                 message=message)))

    @log
    def start_reader_mode(self):
        while True:
            print(self.receive_server_response())

    @log
    def main(self):
        # Parse script arguments
        self.parse_arguments()

        if self.server_ip is None:
            return

        # Create socket and connect to server
        self.socket = self.get_client_socket()

        self.user_name = input("Enter your name: ")

        # Send presence message
        self.send_message(json(get_presence_message(self.user_name, 'Active')))

        # Receive server answer to presence message
        print(self.receive_server_response())

        if self.rw_status == 'w':
            self.start_writer_mode()
        elif self.rw_status == 'r':
            self.start_reader_mode()

        self.socket.close()


if __name__ == "__main__":
    client = Client()
    client.main()
