import unittest
import sqlite3
import sql

class TestLCC(unittest.TestCase):

    def test_valid_adding_product1(self):
        try:
            session = sql.DB_SESSION(sqlite3.connect('lcc'))
            items = ("Subaru","1100","Legacy","1234qwe","1990")
            session._add_product(items)
        except BaseException:
            self.assertTrue(0)

    def test_invalid_year_adding_product(self):
        session = sql.DB_SESSION(sqlite3.connect('lcc'))
        items = ("Subaru","1100","Legacy","1234qwe","90")
        self.assertRaises(BaseException, session._add_product(items))

    def test_invalid_price_adding_product(self):
        session = sql.DB_SESSION(sqlite3.connect('lcc'))
        items = ("subaru","aa","legacy","1234qwe","90")
        self.assertRaises(BaseException, session._add_product(items))

    def test_invalid_license_adding_product(self):
        session = sql.DB_SESSION(sqlite3.connect('lcc'))
        items = ("subaru","1100","legacy","kahsdfadsf","90")
        self.assertRaises(BaseException, session._add_product(items))

    def test_invalid_year_high_adding_product(self):
        session = sql.DB_SESSION(sqlite3.connect('lcc'))
        items = ("subaru","1100","legacy","1234qwe","200000")
        self.assertRaises(BaseException, session._add_product(items))

    def test_invalid_company_adding_product(self):
        session = sql.DB_SESSION(sqlite3.connect('lcc'))
        items = ("34%3444","1100","legacy","1234qwe","1990")
        self.assertRaises(BaseException, session._add_product(items))

    def test_invalid_price_adding_product(self):
        session = sql.DB_SESSION(sqlite3.connect('lcc'))
        items = ("subaru","aa","legacy","1234qwe","1990")
        self.assertRaises(BaseException, session._add_product(items))

    def test_invalid_price_adding_product(self):
        session = sql.DB_SESSION(sqlite3.connect('lcc'))
        items = ("subaru","aa","legacy","1234qwe","1990")
        self.assertRaises(BaseException, session._add_product(items))

    def test_valid_price_adding_product2(self):
        try:
            session = sql.DB_SESSION(sqlite3.connect('lcc'))
            items = ("Subaru",".11","Legacy","1234qwe","1990")
            session._add_product(items)
        except BaseException:
            self.assertTrue(0)

    def test_invalid_year_2_adding_product(self):
        session = sql.DB_SESSION(sqlite3.connect('lcc'))
        items = ("Subaru","1100","Legacy","1234qwe","-9")
        self.assertRaises(BaseException, session._add_product(items))

    def test_invalid_price_2_adding_product(self):
        session = sql.DB_SESSION(sqlite3.connect('lcc'))
        items = ("subaru","uu**8","legacy","1234qwe","90")
        self.assertRaises(BaseException, session._add_product(items))

    def test_invalid_license_2_adding_product(self):
        session = sql.DB_SESSION(sqlite3.connect('lcc'))
        items = ("subaru","1100","legacy","_","90")
        self.assertRaises(BaseException, session._add_product(items))

    def test_invalid_year_2_high_adding_product(self):
        session = sql.DB_SESSION(sqlite3.connect('lcc'))
        items = ("subaru","1100","legacy","1234qwe","-20a")
        self.assertRaises(BaseException, session._add_product(items))

    def test_invalid_company_2_adding_product(self):
        session = sql.DB_SESSION(sqlite3.connect('lcc'))
        items = ("_","1100","legacy","1234qwe","1990")
        self.assertRaises(BaseException, session._add_product(items))

    def test_invalid_price_2_adding_product(self):
        session = sql.DB_SESSION(sqlite3.connect('lcc'))
        items = ("subaru","","legacy","1234qwe","1990")
        self.assertRaises(BaseException, session._add_product(items))

    def test_invalid_price_adding_product(self):
        session = sql.DB_SESSION(sqlite3.connect('lcc'))
        items = ("subaru","aa","legacy","1234qwe","1990")
        self.assertRaises(BaseException, session._add_product(items))

if __name__ == '__main__':
    unittest.main()
