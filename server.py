# Server program

from socket import socket, AF_INET, SOCK_STREAM

# Create TCP socket at localhost:7777 and wait for 3 or less connections
s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 7777))
s.listen(3)

while True:
    # Accept client and get its socket and address
    client, address = s.accept()
    print("Received connection request from %s" % str(address))

    # Send message to client
    answer_str = "Server answers"
    client.send(answer_str.encode('ascii'))

    client.close()
