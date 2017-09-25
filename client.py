# Client program

from socket import socket, AF_INET, SOCK_STREAM

# Create socket and connect to server
s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 7777))

# Receive, decode and print server answer
answer = s.recv(1024)
print(answer.decode("ascii"))

s.close()
