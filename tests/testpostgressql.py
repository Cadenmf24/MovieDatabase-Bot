import unittest
import src.utils

class TestPostgreSQL(unittest.TestCase):

    def test_can_connect(self):
        conn = src.utils.connect()
        cur = conn.cursor()
        cur.execute('SELECT VERSION()')
        self.assertTrue(cur.fetchone()[0].startswith('PostgreSQL'))
        conn.close()

if __name__ == '__main__':
    unittest.main()