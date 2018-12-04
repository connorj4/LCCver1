import unittest
import sqlite3
import sql

class TestLCC(unittest.TestCase):

    def test_adding_product1(self):
        try:
            session = sql.DB_SESSION(sqlite3.connect('lcc'))
            items = ("Subaru","1100","Legacy","1234qwe","1990")
            session._add_product(items)
        except BaseException:
            self.assertTrue(0)

    def test_adding_product2(self):
        try:
            session = sql.DB_SESSION(sqlite3.connect('lcc'))
            items = ("Subaru","adfads","Legacy","1234qwe","1990")
            session._add_product(items)
        except BaseException:
            self.assertTrue(0)

if __name__ == '__main__':
    unittest.main()
