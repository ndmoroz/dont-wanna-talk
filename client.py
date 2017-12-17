# Client program
from socket import socket, AF_INET, SOCK_STREAM
from json_creator import \
    json, \
    get_presence_message, \
    get_message, \
    get_all_contacts_message, \
    get_contacts_message, \
    get_contact_name, \
    get_add_friend_message, \
    get_message_type, \
    get_message_sendfrom, \
    get_message_text, \
    get_quantity, \
    is_message_response, \
    JimAction, \
    JimField
import argparse
from gui.qt_chat_view import QtChatView
from threading import Thread
from ast import literal_eval as str_to_dict
from PyQt5.QtCore import pyqtSignal, QObject
from time import sleep


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
            sleep(0.1)
            resp = self.client.rfile.readline().strip()
            # resp = self.client.rfile.readline()
            # if not resp:
            #     continue
            # resp = resp.strip()
            message = resp.decode('utf-8')
            self.client.messages.append(message)
            if resp:
                print('Received:', message)
                message_dict = str_to_dict(message)

                if is_message_response(message_dict):
                    if JimField.quantity in message:
                        contact_count = get_quantity(message_dict)
                        if contact_count == 0:
                            self.client.contacts_reception_finished = True

                else:
                    message_type = get_message_type(message_dict)
                    if message_type == JimAction.msg:
                        msg_from = get_message_sendfrom(message_dict)
                        msg_text = get_message_text(message_dict)
                        self.client.print_message.emit(msg_from, msg_text)

                    elif message_type == JimAction.contact_list:
                        contact = get_contact_name(message_dict)
                        self.client.contacts.append(contact)
                        contact_count = contact_count - 1
                        if contact_count == 0:
                            self.client.contacts_reception_finished = True


class Client(QObject):
    print_message = pyqtSignal(str, str)

    def __init__(self):
        super().__init__()
        self.view = QtChatView()
        self.view.set_client(self)
        self.messages = []
        self.contacts = []
        self.contacts_reception_finished = False

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

    def get_all_contacts(self):
        self.contacts_reception_finished = False
        self.contacts = []
        get_contacts_message = json(get_all_contacts_message())
        self.send_message(get_contacts_message)
        while True:
            if self.contacts_reception_finished:
                break
        if self.user_name in self.contacts:
            self.contacts.remove(self.user_name)
        return self.contacts

    def get_friend_list(self):
        self.contacts_reception_finished = False
        self.contacts = []
        get_friends_message = json(get_contacts_message())
        self.send_message(get_friends_message)
        while True:
            if self.contacts_reception_finished:
                break
        return self.contacts

    def write_message(self, destination, message):
        self.send_message(
            json(get_message(send_to=destination,
                             send_from=self.user_name,
                             message=message)))

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

        self.view.show_chat(self.user_name)

        self.socket.close()

    def add_friend(self, new_friend):
        add_friend_message = json(get_add_friend_message(new_friend))
        self.send_message(add_friend_message)


if __name__ == "__main__":
    client = Client()
    client.main()
