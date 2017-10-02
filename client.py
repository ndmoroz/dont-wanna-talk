# Client program
from socket import socket, AF_INET, SOCK_STREAM
from json_creator import get_presence_json
import sys


def get_server_ip_port(sys_argv):
    arguments = sys_argv
    server_ip = str(arguments[1]) if len(arguments) > 1 else None
    server_port = int(arguments[2]) if (len(arguments) > 2) else 7777
    return server_ip, server_port


def get_client_socket(server_ip, server_port):
    client_socket = socket(AF_INET, SOCK_STREAM)
    client_socket.connect((server_ip, server_port))
    return client_socket


def main():
    # Parse script arguments
    server_ip, server_port = get_server_ip_port(sys.argv)
    if server_ip is None:
        return

    # Create socket and connect to server
    s = get_client_socket(server_ip, server_port)

    # Send presence message
    s.send(get_presence_json("First", "Nah").encode('utf-8'))

    # Receive server answer to presence message
    presence_response = s.recv(1024)
    print(presence_response.decode("utf-8"))

    s.close()


if __name__ == "__main__":
    main()
