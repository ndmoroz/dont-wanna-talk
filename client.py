# Client program
from socket import socket, AF_INET, SOCK_STREAM
from json_creator import json, get_presence_json
import sys
import log_config

log = log_config.Log('server')


@log
def get_server_ip_port(sys_argv):
    arguments = sys_argv
    server_ip = str(arguments[1]) if len(arguments) > 1 else None
    server_port = int(arguments[2]) if (len(arguments) > 2) else 7777
    return server_ip, server_port


@log
def get_client_socket(server_ip, server_port):
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((server_ip, server_port))
    return client_socket


@log
def send_presence_message(client_socket):
    client_socket.send(json(get_presence_json("First", "Nah")).encode('utf-8'))


@log
def receive_server_response(client_socket):
    return client_socket.recv(1024).decode("utf-8")


def main():
    # Parse script arguments
    server_ip, server_port = get_server_ip_port(sys.argv)
    if server_ip is None:
        return

    # Create socket and connect to server
    with get_client_socket(server_ip, server_port) as s:
        # Send presence message
        send_presence_message(s)

        # Receive server answer to presence message
        print(receive_server_response(s))

        s.close()


if __name__ == "__main__":
    main()
