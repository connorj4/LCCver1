#guilistview.py
from tkinter import Frame, LEFT, YES, BOTH, Label, RAISED, X, Listbox, FLAT
from tkinter import FALSE, Y, Scrollbar, VERTICAL, END
class MultiListbox(Frame):
    """MultiListbox made by Labels as table header and Listbox as table colomns"""
    def __init__(self, master, lists):
        """hi"""
        Frame.__init__(self, master)
        self.lists = []
        for l, w in lists:
            frame = Frame(self)
            frame.pack(side=LEFT, expand=YES, fill=BOTH)
            Label(frame, text=l, borderwidth=1, relief=RAISED).pack(fill=X)
            lb = Listbox(frame, width=w, borderwidth=0, selectborderwidth=0,
                         relief=FLAT, exportselection=FALSE)
            lb.pack(expand=YES, fill=BOTH)
            self.lists.append(lb)
            lb.bind('<B1-Motion>', lambda e, s=self: s._select(e.y))
            lb.bind('<Button-1>', lambda e, s=self: s._select(e.y))
            lb.bind('<Leave>', lambda e: 'break')
            lb.bind('<B2-Motion>', lambda e, s=self: s._b2motion(e.x, e.y))
            lb.bind('<Button-2>', lambda e, s=self: s._button2(e.x, e.y))
        frame = Frame(self)
        frame.pack(side=LEFT, fill=Y)
        Label(frame, borderwidth=1, relief=RAISED).pack(fill=X)
        sb = Scrollbar(frame, orient=VERTICAL, command=self._scroll)
        sb.pack(expand=YES, fill=Y)
        self.lists[0]['yscrollcommand'] = sb.set

    def _select(self, y):
        """select rows"""
        row = self.lists[0].nearest(y)
        self.selection_clear(0, END)
        self.selection_set(row)
        return 'break'

    def _button2(self, x, y):
        """allows the canvas to be clickable"""
        for l in self.lists:
            l.scan_mark(x, y)
        return 'break'

    def _b2motion(self, x, y):
        """canvas can be dragged"""
        for l in self.lists:
            l.scan_dragto(x, y)
        return 'break'

    def _scroll(self, *args):
        """scroll through the list of records"""
        for l in self.lists:
            l.yview(*args)

    def curselection(self):
        """returns user's selection"""
        return self.lists[0].curselection()

    def delete(self, first, last=None):
        """delete a record"""
        for l in self.lists:
            l.delete(first, last)

    def get(self, first, last=None):
        """get results"""
        result = []
        for l in self.lists:
            result.append(l.get(first, last))
        if last:
            return list(map(*[None] + result))
        return result
    def index(self, index):
        """adds record to index"""
        self.lists[0].index(index)

    def insert(self, index, *elements):
        """add new records"""
        for e in elements:
            i = 0
            for l in self.lists:
                l.insert(index, e[i])
                i = i + 1

    def size(self):
        """resize the canvas"""
        return self.lists[0].size()

    def see(self, index):
        """display records"""
        for l in self.lists:
            l.see(index)

    def selection_anchor(self, index):
        """highlights selection"""
        for l in self.lists:
            l.selection_anchor(index)

    def selection_clear(self, first, last=None):
        """clear selection of records"""
        for l in self.lists:
            l.selection_clear(first, last)

    def selection_includes(self, index):
        """include selection in the index"""
        return self.lists[0].selection_includes(index)

    def selection_set(self, first, last=None):
        """sets customer name in records"""
        self.item_selected = [first,]+self.get(first)
        for l in self.lists:
            l.selection_set(first, last)
    def not_focus(self):#suhail
        """unfocus selection"""
        for l in self.lists:
            l['takefocus'] = False
    