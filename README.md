# Dont wanna talk

A chat for those who prefer silence.

### System Requirements

* Python 3.6
* SQLAlchemy
* PyQT5

## Launching server

To start server on localhost using port 777:

    python dwt-server.py
    
To start server on localhost using custom port (e.g. 1234):

    python dwt-server.py -p 1234

To start server on localhost using custom port (e.g. 1234) 
and listen to custom ip range (e.g. 10.0.0.1-10.0.0.5):

    python dwt-server.py -p 1234 -a 10.0.0.1-10.0.0.5

## Launching client
    
To start client connecting to chat server on localhost:7777:
    
    python dwt-client.py 10.0.0.1 777

To start client connecting to custom chat server (e.g. 10.0.0.1:1234):
    
    python dwt-client.py 10.0.0.1 1234
