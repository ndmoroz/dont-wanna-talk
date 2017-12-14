import unittest
import subprocess


class TestServerClient(unittest.TestCase):
    def test_reader_gets_writer_message(self):

        try:
            # Launching server, client-writer and client-reader
            # specifying encoding to communicate in strings, not in bytes
            server = subprocess.Popen(['python', 'server.py'],
                                      stdout=subprocess.PIPE,
                                      stdin=subprocess.PIPE,
                                      stderr=subprocess.STDOUT,
                                      encoding='utf-8')

            writer = subprocess.Popen(
                ['python', 'client.py', '-w', 'localhost'],
                stdout=subprocess.PIPE,
                stdin=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                encoding='utf-8')

            writer.stdin.write("writerName\n")
            writer.stdin.flush()

            reader = subprocess.Popen(
                ['python', 'client.py', '-r', 'localhost'],
                stdout=subprocess.PIPE,
                stdin=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                encoding='utf-8')

            reader.stdin.write("readerName\n")
            reader.stdin.flush()

            writer.stdin.write("message1\n")
            writer.stdin.flush()

            while True:
                reader_reception = reader.stdout.readline()
                if "msg" in reader_reception:
                    break

            has_reader_received = \
                '"from": "writerName"' in reader_reception and \
                '"message": "message1"' in reader_reception

            self.assertTrue(has_reader_received)

        except ResourceWarning:
            pass


if __name__ == '__main__':
    unittest.main()
