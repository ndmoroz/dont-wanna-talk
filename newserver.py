# Server program
from socket import socket, AF_INET, SOCK_STREAM
from json_creator import json, get_response_message, JimCode
import argparse
import log_config
from select import select
from socketserver import TCPServer, StreamRequestHandler, ThreadingMixIn

log = log_config.Log('server')


class MessageHandler(StreamRequestHandler):
    def handle(self):
        print('Client connected - {}:{}'.format(*self.client_address))
        self.server.add_client(self)
        while True:
            data = self.rfile.readline().strip()
            client_message = data.decode('utf-8')
            print(client_message)
            self.server.write_to_clients(client_message)
        self.server.remove_client(self)
        print('Client disconnected - {}:{}'.format(*self.client_address))


class Server(ThreadingMixIn, TCPServer):
    allow_reuse_address = True
    max_children = 10

    def __init__(self, server_address, request_handler_class):
        super().__init__(server_address, request_handler_class, True)
        self.clients = set()

    def add_client(self, client):
        self.clients.add(client)

    def remove_client(self, client):
        self.clients.remove(client)

    def write_to_clients(self, message):
        for client in self.clients:
            client.wfile.write((message + '\n').encode('utf-8'))


@log
def get_server_port(**main_args):
    if __name__ == "__main__":
        # Parse script arguments
        arg_parser = argparse.ArgumentParser()
        arg_parser.add_argument('-p')
        arg_parser.add_argument('-a')
        arguments = arg_parser.parse_args()
        server_port = 7777 if (arguments.p is None) else int(arguments.p)
    else:
        # Parse main() arguments
        server_port = main_args.get('p', 7777)
    return server_port


@log
def get_ips_to_listen(**main_args):
    if __name__ == "__main__":
        # Parse script arguments
        arg_parser = argparse.ArgumentParser()
        arg_parser.add_argument('-p')
        arg_parser.add_argument('-a')
        arguments = arg_parser.parse_args()
        ip_to_listen = '' if (arguments.a is None) else str(arguments.a)
    else:
        # Parse main() arguments
        ip_to_listen = main_args.get('a', '')
    return ip_to_listen


@log
def main(**main_args):
    server_port = get_server_port(**main_args)
    ip_to_listen = get_ips_to_listen(**main_args)

    server = Server(('', server_port), MessageHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()
