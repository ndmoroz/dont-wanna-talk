# Server program
from socket import socket, AF_INET, SOCK_STREAM
from json_creator import \
    get_message_type, \
    JimAction, \
    get_username, \
    get_adding_friend_name
import argparse
import log_config
from socketserver import ThreadingTCPServer, StreamRequestHandler
from storage import ServerStorage
from ast import literal_eval as str_to_dict


# log = log_config.Log('server')


class MessageHandler(StreamRequestHandler):
    def _read_message(self):
        try:
            data = self.rfile.readline()
        except:
            return None
        if not data:
            return None
        else:
            data = data.strip()
            client_message = data.decode('utf-8')
            self.server.messages.append((self, client_message))
            print(client_message)
            return str_to_dict(client_message)


    def handle(self):
        print('Client connected - {}:{}'.format(*self.client_address))

        presence_message = self._read_message()
        if presence_message is not None:
            client_id = self.server.get_id_by_presence(presence_message)
            self.server.add_client(self)

            while True:
                message = self._read_message()
                if message is None:
                    break
                else:
                    self.server.parse_client_message(self, client_id, message)

            self.server.remove_client(self)

        print('Client disconnected - {}:{}'.format(*self.client_address))



class Server(ThreadingTCPServer):
    allow_reuse_address = True
    max_children = 10

    def __init__(self, server_address, request_handler_class):
        super().__init__(server_address, request_handler_class, True)
        self.clients = set()
        self.storage = ServerStorage()
        self.messages = []

    def add_client(self, client):
        self.clients.add(client)

    def remove_client(self, client):
        self.clients.remove(client)

    def write_to_client(self, client, message):
        print('Sent:', message)
        client.wfile.write((message + '\n').encode('utf-8'))

    def write_to_all_clients(self, message, sender_client):
        for client in self.clients:
            if client is sender_client:
                continue
            self.write_to_client(client, message)

    def parse_client_message(self, client, client_id, message):
        ip = client.client_address[0]

        message_type = get_message_type(message)
        if message_type == JimAction.presence:
            self.register_client_connect(get_username(message), ip)

        elif message_type == JimAction.get_all_contacts:
            self._send_all_contacts(client)

        elif message_type == JimAction.get_contacts:
            self._send_client_contacts(client, client_id)

        elif message_type == JimAction.add_friend:
            friend_name = get_adding_friend_name(message)
            self._add_client_friend(client_id, friend_name)

        elif message_type == JimAction.msg:
            self.write_to_all_clients(message, client)

    def register_client_connect(self, username, ip):
        self.storage.save_client_connect(username, ip)

    def get_id_by_presence(self, presence_message):
        client_name = get_username(presence_message)
        client_id = self.storage.get_client_id(client_name)
        return client_id

    def _send_all_contacts(self, client):
        all_contacts = self.storage.get_all_contacts()
        contacts = []
        for contact in all_contacts:
            contacts.append(contact)
        contacts_count = len(contacts)
        self.write_to_client(client, 'Start List')
        # self.write_to_client(client, str(contacts_count))
        for contact in contacts:
            self.write_to_client(client, contact)
        self.write_to_client(client, 'End List')

    def _send_client_contacts(self, client, client_id):
        client_friends = self.storage.get_client_friends(client_id)
        contacts = []
        for contact in client_friends:
            contacts.append(contact)
        contacts_count = len(contacts)
        self.write_to_client(client, 'Start List')
        # self.write_to_client(client, str(contacts_count))
        for contact in contacts:
            self.write_to_client(client, contact)
        self.write_to_client(client, 'End List')

    def _add_client_friend(self, client_id, friend_name):
        self.storage.add_new_friend(client_id, friend_name)


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


def main(**main_args):
    server_port = get_server_port(**main_args)
    ip_to_listen = get_ips_to_listen(**main_args)
    server = Server(('', server_port), MessageHandler)
    server.serve_forever()


if __name__ == "__main__":
    main()
