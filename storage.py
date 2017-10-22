from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class ClientServerTable(Base):
    __tablename__ = 'client'

    client_id = Column(Integer, primary_key=True)
    username = Column(String, nullable=False)
    info = Column(String)

    def __init__(self, username, info):
        self.username = username
        self.info = info


class ClientHistoryServerTable(Base):
    __tablename__ = 'client_history'

    client_history_id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('client.client_id'))
    login_time = Column(DateTime, nullable=False)
    ip = Column(String, nullable=False)

    def __init__(self, client_id, ip, time):
        self.client_id = client_id
        self.ip = ip
        self.login_time = time


class ClientFriendsServerTable(Base):
    __tablename__ = 'client_friend'

    client_friend_id = Column(Integer, primary_key=True)
    client_id = Column(Integer, ForeignKey('client.client_id'))
    friend_id = Column(Integer, ForeignKey('client.client_id'))

    def __init__(self, client_id, ip, friend_id):
        self.client_id = client_id
        self.friend_id = friend_id


class FriendsClientTable(Base):
    __tablename__ = 'friend'

    friend_id = Column(Integer, primary_key=True)
    friend_name = Column(String, nullable=False)

    def __init__(self, friend_name):
        self.friend_name = friend_name


class HistoryClientTable(Base):
    __tablename__ = 'history'

    history_id = Column(Integer, primary_key=True)
    sent_to = Column(Integer, ForeignKey('friend.friend_id'))
    message = Column(String, nullable=False)

    def __init__(self, sent_to, message):
        self.sent_to = sent_to
        self.message = message
