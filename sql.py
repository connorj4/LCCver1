"""Inserts, deletes, and updates SQL database"""
import sqlite3

class DB_SESSION:
    """Opens up the SQL Database Session"""
    def __init__(self, conn):
        self.conn = conn
        self.cur = self.conn.cursor()

    def _query(self, q="""SELECT * from invoices"""):
        self.cur.execute(q)
        return self.cur.fetchall()
    def _find_products(self, val):
        print(val)
        self.cur.execute("select * from products where name like '%"+val+"%'")
        return self.cur.fetchall()
    def _find_customers(self, val):
        print(val)
        self.cur.execute("select * from customers where cusname like '%"+val+"%'")
        return self.cur.fetchall()
    def _delete_invoice(self, i_d):
        t = (i_d, )
        self.cur.execute('DELETE FROM invoices WHERE id = ?', t)
        self.cur.execute('DELETE FROM invoiceitems WHERE invoiceid = ?', t)
        self.conn.commit()

    def _add_product(self, items):
        self.cur.execute('select MAX(id) from products')
        i_d = self.cur.fetchone()[0] + 1
        items = (i_d, )+items
        self.cur.execute('INSERT INTO products VALUES (?, ?, ?, ?, ?, ?)', items)
        self.conn.commit()

    def _add_customer(self, items):
        self.cur.execute('select MAX(cusid) from customers')
        i_d = self.cur.fetchone()[0] + 1
        items = (i_d, )+items
        self.cur.execute('INSERT INTO customers VALUES (?, ?, ?)', items)
        self.conn.commit()

    def _add_invoice(self, inv, items):
        #items is a list comprising (id, invoiceid, productid, quantity)
        #inv is a tuple comprising (id,customer, date, amount)
        self.cur.execute('INSERT INTO invoices VALUES (?, ?, ?, ?)', inv)
        for t in items:
            self.cur.execute('INSERT INTO invoiceitems VALUES (?, ?, ?, ?)', t)
        self.conn.commit()
    def _add_product_cmd(self):
        self.cur.execute('select MAX(id) from products')
        i_d = self.cur.fetchone()[0] + 1
        items = []
        while True:
            name = input('Vehicle Model: ')
            if name == '':
                break
            desc = input('Vehicle type: ')
            price = input('Price: ')
            t = (i_d, name, desc, int(price))
            self.cur.execute('insert into products values (?, ?, ?, ?)', t)
            i_d += 1
        self.conn.commit()
    def _show_invoice(self, i_d):
        t = (i_d, )
        self.cur.execute('''select invoiceitems.id, name, quantity, \
        description, price, price * quantity
        from invoiceitems, products
        where invoiceitems.productid = products.id
        and invoiceitems.invoiceid = ?''', t)
        return self.cur.fetchall()
    def _delete_product(self, i_d):
        t = (i_d, )
        self.cur.execute('DELETE FROM products WHERE id = ?', t)
        self.conn.commit()
    def _delete_customer(selfself, i_d):
        t = (i_d, )
        self.cur.execute('DELETE FROM customers WHERE cusid = ?', t)
        self.conn.commit()
    def close(self):
        """close connection with the database"""
        self.conn.close()
    def _next_invoiceid(self):
        self.cur.execute('select MAX(id) from invoices')
        i_d = self.cur.fetchone()[0] + 1
        return i_d

'''   def _add_invoice(self):
        query = "INSERT INTO invoices VALUES (0,'', 0, 0)"
        c =s elf.conn.cursor()
        c.execute(query)
        self.conn.commit()
        print (self._last_rowid())                       
    def _add_invoice_items(self):
        pass    
    def _update(self):
        query = 'UPDATE invoices SET invoiceid = 4 WHERE id = "Smith"';        
    def _last_rowid(self):
        return int(self.c.lastrowid)'''

session = DB_SESSION(sqlite3.connect('lcc'))
