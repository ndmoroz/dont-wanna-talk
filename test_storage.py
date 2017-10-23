import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import storage
import datetime


class TestServerTable(unittest.TestCase):
    def setUp(self):
        self.engine = create_engine('sqlite:///:memory:')
        session = sessionmaker(bind=self.engine)
        storage.Base.metadata.create_all(self.engine)
        self.session = session()
        self.client1 = storage.ClientServerTable \
            ('FirstInTable', 'Not very sociable')
        self.client2 = storage.ClientServerTable \
            ('SecondComing', 'Not very sociable either')
        self.session.add(self.client1)
        self.session.add(self.client2)
        self.session.commit()

    def tearDown(self):
        storage.Base.metadata.drop_all(self.engine)

    def test_reading_two_clients(self):
        result = self.session.query(storage.ClientServerTable).all()
        client = result[0]
        self.assertEqual(client.username, self.client1.username)
        self.assertEqual(client.info, self.client1.info)
        client = result[1]
        self.assertEqual(client.username, self.client2.username)
        self.assertEqual(client.info, self.client2.info)

    def test_writing_reading_client_history(self):
        self.history = storage.ClientHistoryServerTable \
            (1, '192.168.0.1', datetime.datetime.utcnow())
        self.session.add(self.history)
        self.session.commit()
        expected = [self.history]
        result = self.session.query(storage.ClientHistoryServerTable).all()
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
