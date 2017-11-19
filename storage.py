from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine, exists
from sqlalchemy.orm import sessionmaker, load_only
from datetime import datetime

ServerBase = declarative_base()
ClientBase = declarative_base()


class ServerStorage:
    def __init__(self):
        engine = create_engine('sqlite:///server.sqlite')
        session = sessionmaker(bind=engine)
        ServerBase.metadata.create_all(engine)
        self.session = session()

    def save_client_connect(self, username, ip):
        client_id = self._get_client_id(username)
        if client_id is None:
            self.save_new_client(username)
            client_id = self._get_client_id(username)
        history = ClientHistoryServerTable(client_id, ip, datetime.utcnow())
        self.session.add(history)
        self._save_changes()

    def save_new_client(self, username):
        info = 'First connect (UTC): ' + str(datetime.utcnow())
        client = ClientServerTable(username, info)
        self.session.add(client)
        self._save_changes()

    def _get_client_id(self, username):
        client = self.session.query(ClientServerTable)
        client = client.filter(ClientServerTable.username == username)
        client = client.first()
        if client is not None:
            return client.client_id

    def get_all_contacts(self):
        clients = []
        for client in self.session. \
                query(ClientServerTable).options(load_only("username")):
            clients.append(client.username)
        return clients

    def _save_changes(self):
        self.session.commit()


class ClientServerTable(ServerBase):
    __tablename__ = 'client'

    client_id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    info = Column(String)

    def __init__(self, username, info):
        self.username = username
        self.info = info


class ClientHistoryServerTable(ServerBase):
    __tablename__ = 'client_history'

    client_history_id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('client.client_id'))
    login_time = Column(DateTime, nullable=False)
    ip = Column(String, nullable=False)

    def __init__(self, client_id, ip, time):
        self.client_id = client_id
        self.ip = ip
        self.login_time = time


class ClientFriendsServerTable(ServerBase):
    __tablename__ = 'client_friend'

    client_friend_id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('client.client_id'))
    friend_id = Column(Integer, ForeignKey('client.client_id'))

    def __init__(self, client_id, ip, friend_id):
        self.client_id = client_id
        self.friend_id = friend_id


class FriendsClientTable(ClientBase):
    __tablename__ = 'friend'

    friend_id = Column(Integer, primary_key=True)
    friend_name = Column(String, nullable=False)

    def __init__(self, friend_name):
        self.friend_name = friend_name


class HistoryClientTable(ClientBase):
    __tablename__ = 'history'

    history_id = Column(Integer, primary_key=True)
    sent_to = Column(Integer, ForeignKey('friend.friend_id'))
    message = Column(String, nullable=False)

    def __init__(self, sent_to, message):
        self.sent_to = sent_to
        self.message = message
