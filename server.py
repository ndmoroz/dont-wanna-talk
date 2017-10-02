# Server program
from socket import socket, AF_INET, SOCK_STREAM
from json_creator import get_empty_response_json, JimCode
import argparse


class Server:
    def __init__(self):
        self.stopped = False

    def stop(self):
        self.stopped = True

    def main(self, **main_args):
        if __name__ == "__main__":
            # Parse script arguments
            arg_parser = argparse.ArgumentParser()
            arg_parser.add_argument('-p', action='store')
            arg_parser.add_argument('-a', action='store')
            arguments = arg_parser.parse_args()
            server_port = 7777 if (arguments.p is None) else int(arguments.p)
            ip_to_listen = '' if (arguments.a is None) else str(arguments.a)
        else:
            # Parse main() arguments
            server_port = main_args.get('p', 7777)
            ip_to_listen = main_args.get('a', '')

        # Create TCP socket at localhost:7777 and wait for 3 or less connections
        s = socket(AF_INET, SOCK_STREAM)
        s.bind(('', server_port))
        s.listen(3)

        while not self.stopped:
            # Accept client and get its socket and address
            client, address = s.accept()

            if len(ip_to_listen) > 0 and address[0] != ip_to_listen:
                client.close()
                continue

            print("Received connection request from %s" % str(address))

            # Receive presence message
            client_presence = client.recv(1024)
            print(client_presence.decode("utf-8"))

            # Send OK answer
            client.send(get_empty_response_json(JimCode.ok).encode('utf-8'))

            client.close()


if __name__ == "__main__":
    Server.main()
