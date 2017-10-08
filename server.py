# Server program
from socket import socket, AF_INET, SOCK_STREAM
from json_creator import json, get_empty_response_json, JimCode
import argparse
import log_config
from select import select

log = log_config.Log('server')


class Server:
    def __init__(self):
        self.stopped = False

    def stop(self):
        self.stopped = True

    @log
    def get_server_port(self, **main_args):
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
    def get_ips_to_listen(self, **main_args):
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
    def get_server_socket(self, server_port, max_connections):
        s = socket(AF_INET, SOCK_STREAM)
        s.bind(('', server_port))
        s.listen(max_connections)
        s.settimeout(0.001)
        return s

    @log
    def get_client_message(self, client_socket):
        return client_socket.recv(1024).decode("utf-8")

    @log
    def send_client_message(self, client_socket, message):
        client_socket.send(message.encode('utf-8'))

    @log
    def main(self, **main_args):
        server_port = self.get_server_port(**main_args)
        ip_to_listen = self.get_ips_to_listen(**main_args)

        # Create TCP socket at localhost:7777 and wait for 3 or less connections
        s = self.get_server_socket(server_port, 3)

        clients = []

        while not self.stopped:
            try:
                # Accept client and get its socket and address
                client, address = s.accept()
            except:
                pass
            else:
                if len(ip_to_listen) > 0 and address[0] != ip_to_listen:
                    client.close()
                    continue

                print("Received connection request from %s" % str(address))

                # Receive presence message
                client_message = self.get_client_message(client)
                print(client_message)

                # Send OK answer
                self.send_client_message(client,
                                         json(get_empty_response_json(
                                             JimCode.ok)))

                clients.append(client)

            r = []
            w = []
            message = ''

            try:
                r, w, e = select(clients, clients, [], 0)
            except:
                pass

            for client in r:
                try:
                    message = self.get_client_message(client)
                except:
                    print('cant read, closing client')
                    client.close()
                    clients.remove(client)
                else:
                    print(message)

            for client in w:
                try:
                    self.send_client_message(client, message)
                except:
                    print('cant write, closing client')
                    client.close()
                    clients.remove(client)

                    # while True:
                    #     # Receive presence message
                    #     client_message = self.get_client_message(client)
                    #     print(client_message)


if __name__ == "__main__":
    server = Server()
    server.main()
