# Server program
from socket import socket, AF_INET, SOCK_STREAM
from json_creator import get_message_type, JimAction, get_username
import argparse
import log_config
from socketserver import TCPServer, StreamRequestHandler, ThreadingMixIn
from storage import ServerStorage
from ast import literal_eval as str_to_dict

log = log_config.Log('server')


class MessageHandler(StreamRequestHandler):
    def handle(self):
        print('Client connected - {}:{}'.format(*self.client_address))
        self.server.add_client(self)
        while True:
            data = self.rfile.readline().strip()
            client_message = data.decode('utf-8')
            print(client_message)
            client_message_dict = str_to_dict(client_message)
            self.server.parse_client_message(self, client_message_dict)
            self.server.write_to_all_clients(client_message)
        self.server.remove_client(self)
        print('Client disconnected - {}:{}'.format(*self.client_address))


class Server(ThreadingMixIn, TCPServer):
    allow_reuse_address = True
    max_children = 10

    def __init__(self, server_address, request_handler_class):
        super().__init__(server_address, request_handler_class, True)
        self.clients = set()
        self.storage = ServerStorage()

    def add_client(self, client):
        self.clients.add(client)

    def remove_client(self, client):
        self.clients.remove(client)

    def write_to_client(self, client, message):
        print('Sent:', message)
        client.wfile.write((message + '\n').encode('utf-8'))

    def write_to_all_clients(self, message):
        for client in self.clients:
            self.write_to_client(client, message)

    def parse_client_message(self, client, message):
        ip = client.client_address[0]
        message_type = get_message_type(message)
        if message_type == JimAction.presence:
            self.register_client_connect(get_username(message), ip)
        elif message_type == JimAction.get_all_contacts:
            self._send_all_contacts(client)

    def register_client_connect(self, username, ip):
        self.storage.save_client_connect(username, ip)

    def _send_all_contacts(self, client):
        all_contacts = self.storage.get_all_contacts()
        contacts = []
        for contact in all_contacts:
            contacts.append(contact)
        contacts_count = len(contacts)
        self.write_to_client(client, str(contacts_count))
        for contact in contacts:
            self.write_to_client(client, contact)


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
