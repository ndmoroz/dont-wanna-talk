# Dont wanna talk

A chat for those who prefer silence.

### System Requirements

* Python 3.6
* SQLAlchemy
* PyQT5

## Launching server

To start server on localhost using port 777:

    python server.py
    
To start server on localhost using custom port (e.g. 1234):

    python server.py -p 1234

## Launching client
    
To start client connecting to chat server on localhost:7777:
    
    python client.py

To start client connecting to custom chat server (e.g. 10.0.0.1:1234):
    
    python client.py 10.0.0.1 1234
    
### Exemplary server database

This repository contains exemplary database to test chat 
with following contacts:

Bill has friends: 
* Alfred 
* Jimmy
* Monique
* Hillary

Monique has friends: 
* Alfred
* Jimmy
* Bill
