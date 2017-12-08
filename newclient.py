# Client program
from socket import socket, AF_INET, SOCK_STREAM
from json_creator import \
    json, \
    get_presence_message, \
    get_message, \
    get_all_contacts_message, \
    get_contacts_message, \
    get_contact_name, \
    get_add_friend_message
import log_config
import argparse
from gui.qt_chat_view import QtChatView
from threading import Thread


# log = log_config.Log('client')


class SendThread(Thread):
    def __init__(self, client):
        Thread.__init__(self)
        self.client = client
        self.is_stopped = False
        self.setDaemon(True)

    def run(self):
        while not self.is_stopped:
            msg = self.client.msg_queue.get()
            print('sending:', msg)
            self.client.sock.send(msg.utf8)
            self.client.msg_queue.task_done()


class ReceiveThread(Thread):
    def __init__(self, client_socket):
        Thread.__init__(self)
        self.client = client
        self.is_stopped = False
        self.setDaemon(True)

    def run(self):
        while not self.is_stopped:
            resp = self.client.rfile.readline().strip()
            message = resp.decode('utf-8')
            self.client.messages.append(message)
            if resp:
                print('Received:', message)


class Client:
    def __init__(self):
        self.view = QtChatView()
        self.view.set_client(self)
        self.messages = []

    def parse_arguments(self):
        arg_parser = argparse.ArgumentParser()
        arg_parser.add_argument('-r', action='count')
        arg_parser.add_argument('-w', action='count')
        arg_parser.add_argument('ip', nargs='?', default='localhost')
        arg_parser.add_argument('port', nargs='?', default=7777)
        arguments = arg_parser.parse_args()
        print(arguments)
        self.server_ip = str(arguments.ip)
        self.server_port = int(arguments.port)
        self.rw_status = 'r' if arguments.w is None else 'w'

    def get_client_socket(self):
        client_socket = socket(AF_INET, SOCK_STREAM)
        client_socket.connect((self.server_ip, self.server_port))
        return client_socket

    def send_message(self, message):
        self.wfile.write((message + '\n').encode('utf-8'))

    def send_message_old(self, message):
        self.socket.sendall(bytes(message, 'utf-8'))

    def receive_server_response(self):
        return self.rfile.readline().strip().decode('utf-8')

    def receive_server_response_old(self):
        return str(self.socket.recv(1024), 'utf-8')

    def start_writer_mode(self):
        self.view.show_chat()

    def get_all_contacts(self):
        get_contacts_message = json(get_all_contacts_message())
        self.send_message(get_contacts_message)
        contacts = []
        i = 0
        while True:
            message = self.messages.pop()
            if 'Start List' in message:
                break
        while True:
            message = self.messages.pop()
            if message:
                print('Parsing [', message, ']')
                if 'End List' in message:
                    break
                contacts.append(message)
        return contacts

    def get_friend_list(self):
        get_friends_message = json(get_contacts_message())
        self.send_message(get_friends_message)
        contacts = []
        i = 0
        while True:
            if len(self.messages) > i:
                message = self.messages[i]
                i = i + 1
                if 'Start List' in message:
                    break
        while True:
            if len(self.messages) > i:
                message = self.messages[i]
                print('Parsing [', message, ']')
                if 'End List' in message:
                    break
                contacts.append(message)
                i = i + 1
        return contacts

    def write_message(self, message):
        self.send_message(
            json(get_message(send_to='Agora',
                             send_from=self.user_name,
                             message=message)))

    def start_reader_mode(self):
        self.view.show_chat()
        # while True:
        #     self.view.print_message(self.receive_server_response())

    def main(self):
        # Parse script arguments
        self.parse_arguments()

        if self.server_ip is None:
            return

        # Create socket and connect to server
        self.socket = self.get_client_socket()
        self.socket.setblocking(False)
        self.rfile = self.socket.makefile('rb', -1)
        self.wfile = self.socket.makefile('wb', 0)

        # self.user_name = input("Enter your name: ")

        self.user_name = self.view.get_username()

        # Send presence message
        self.send_message(json(get_presence_message(self.user_name, 'Active')))
        # Receive server answer to presence message
        # print(self.receive_server_response())

        self.recv_thread = ReceiveThread(self)
        self.recv_thread.start()

        if self.rw_status == 'w':
            self.start_writer_mode()
        elif self.rw_status == 'r':
            self.start_reader_mode()

        self.socket.close()

    def add_friend(self, new_friend):
        add_friend_message = json(get_add_friend_message(new_friend))
        self.send_message(add_friend_message)


if __name__ == "__main__":
    client = Client()
    client.main()
