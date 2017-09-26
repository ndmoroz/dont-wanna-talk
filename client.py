# Client program
from socket import socket, AF_INET, SOCK_STREAM
from json_creator import get_presence_json
import sys

# Parse script arguments
arguments = sys.argv
server_ip = str(arguments[1])
server_port = 7777 if (len(arguments) == 2) else int(arguments[2])

# Create socket and connect to server
s = socket(AF_INET, SOCK_STREAM)
s.connect((server_ip, server_port))

# Send presence message
s.send(get_presence_json("First", "Nah").encode('utf-8'))

# Receive server answer to presence message
presence_response = s.recv(1024)
print(presence_response.decode("utf-8"))

s.close()
