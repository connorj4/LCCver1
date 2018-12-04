#from binascii import a2b_qp
# final from 20/09/2018. To jest ostateczna wersja
import sqlite3
import gui

###simple password checking method
def haslo():
    """Authenticates user and connects to SQL Database"""
    a = input("Admin: ")
    p = input("Password: ")
    if a == "admin" and p == "admin":
        print("Ok, you can go")
        root = gui.Tk()
        root['bg'] = 'black'
        frmenu = gui.FormMenu(root)
        # frmmenu._init_menu()
        frmenu._init_widgets()

        conn = sqlite3.connect("lcc")
        cur = conn.cursor()
        cur.execute("select* from invoices")
        print(cur.fetchone()[1])
        root.mainloop()
    else:
        print("Nope, you are not the right person")
        raise NameError("Invalid")
haslo()
root = gui.Tk()
#frame = gui.MyFrame(root)
#frame.pack()

root['bg'] = 'black'
frmenu = gui.FormMenu(root)
#frmmenu._init_menu()
frmenu._init_widgets()

conn = sqlite3.connect("lcc")
cur = conn.cursor()
cur.execute("select* from invoices")
print(cur.fetchone()[1])
if __name__ == "__main__":
    #Example(root).pack(fill="both", expand=True)
    root.mainloop()

"""
#End Code