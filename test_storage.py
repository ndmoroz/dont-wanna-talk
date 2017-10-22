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

    def tearDown(self):
        storage.Base.metadata.drop_all(self.engine)

    def test_create_client(self):
        self.client = storage.ClientServerTable \
            ('FirstInTable', 'Not very sociable')
        self.session.add(self.client)
        self.session.commit()
        expected = [self.client]
        result = self.session.query(storage.ClientServerTable).all()
        self.assertEqual(result, expected)

    def test_create_client(self):
        self.history = storage.ClientHistoryServerTable \
            (1, '192.168.0.1', datetime.datetime.utcnow())
        self.session.add(self.history)
        self.session.commit()
        expected = [self.history]
        result = self.session.query(storage.ClientHistoryServerTable).all()
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
