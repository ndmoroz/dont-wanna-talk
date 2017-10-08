# Client program
from socket import socket, AF_INET, SOCK_STREAM
from json_creator import json, get_presence_json, get_chatroom_message
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
    def get_client_socket(self, server_ip, server_port):
        client_socket = socket(AF_INET, SOCK_STREAM)
        client_socket.connect((server_ip, server_port))
        return client_socket

    @log
    def send_message(self, client_socket, message):
        client_socket.send(message.encode('utf-8'))

    @log
    def receive_server_response(self, client_socket):
        return client_socket.recv(1024).decode("utf-8")

    @log
    def main(self):
        # Parse script arguments
        self.parse_arguments()
        print(self.server_ip)
        print(self.server_port)
        print(self.rw_status)

        if self.server_ip is None:
            return

        # Create socket and connect to server
        with self.get_client_socket(self.server_ip, self.server_port) as s:
            user_name = input("Enter your name: ")

            # Send presence message
            self.send_message(s, json(get_presence_json(user_name, 'Active')))

            # Receive server answer to presence message
            print(self.receive_server_response(s))

            message = input("Your message: ")

            self.send_message(s, json(get_chatroom_message(chatroom='Agora',
                                                           username=user_name,
                                                           message=message)))

        s.close()


if __name__ == "__main__":
    client = Client()
    client.main()
