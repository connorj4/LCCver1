from tkinter import *
def _init_toolbar(tbmaster):
    
    '''Menu has buttons to ADD, EDIT, DELETE AND FIND
        the argument is a class and it must have:
        tbmaster.frame              :- a root window class
        tbmaster.btn_add_click()    :- a method
        tbmaster.btn_edit_click()
        tbmaster.btn_delete_click()
        tbmaster.btn_find_click()
        '''
    tbmaster.tb=Frame(tbmaster.frame,borderwidth=1)
    tbmaster.tb.configure(background="grey90",bd=0)
    tbmaster.tb.pack(side=TOP,fill=X)
    
    tbmaster.btn_add=Button(tbmaster.tb,bg="grey90",bd=0,cursor="hand1",text="Add",compound="bottom",command=tbmaster.btn_add_click)
    tbmaster.imgadd=PhotoImage(file="images/add.gif")
    tbmaster.btn_add['image']=tbmaster.imgadd
    tbmaster.btn_add.pack(side=LEFT,padx=4,pady=4)
    
    tbmaster.btn_edit=Button(tbmaster.tb,bg="grey90",bd=0,cursor="hand1",text="Edit",compound="bottom",command=tbmaster.btn_edit_click)
    tbmaster.imgedit=PhotoImage(file="images/edit.gif")
    tbmaster.btn_edit['image']=tbmaster.imgedit
    tbmaster.btn_edit.pack(side=LEFT,padx=4,pady=4)
    
    tbmaster.btn_delete=Button(tbmaster.tb,bg="grey90",bd=0,cursor="hand1",text="Delete",compound="bottom",command=tbmaster.btn_del_click)
    tbmaster.imgdel=PhotoImage(file="images/delete.gif")
    tbmaster.btn_delete['image']=tbmaster.imgdel
    tbmaster.btn_delete.pack(side=LEFT,padx=4,pady=4)

    tbmaster.entryfind=Entry(tbmaster.tb, width=60, bg="grey98", cursor="text", selectbackground="grey99")
    tbmaster.entryfind.pack(side=LEFT,padx=4,pady=4)
    
    tbmaster.btn_find=Button(tbmaster.tb,bg="grey90",bd=0,cursor="hand1",text="Search",compound="bottom",command=tbmaster.btn_find_click)
    tbmaster.imgfind=PhotoImage(file="images/search.gif")
    tbmaster.btn_find['image']=tbmaster.imgfind
    tbmaster.btn_find.pack(side=LEFT,padx=4,pady=4)
    
    tbmaster.entryfind=Entry(tbmaster.tb)


