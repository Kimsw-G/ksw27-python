import tkinter
from tkinter import ttk
from repo.student_repo import student_repo

class list_frame:
    def __init__(self,window):
        self.s_repo = student_repo()
        self.frame = ttk.Frame(window)
        self.frame.grid(row=1, column=0, sticky="nsew")
        ttk.Label(self.frame, text="학생리스트").grid(row=1, column=0)
        self.trv = ttk.Treeview(self.frame,columns=["stdNo","이름","ID"],displaycolumns=["stdNo","이름","ID"])
        self.trv.column("#0", width=100)
        self.trv.heading("#0", text="index")
        self.trv.column("#1", width=100, anchor="center")
        self.trv.heading("stdNo", text="stdNo", anchor="center")
        self.trv.column("#2", width=150, anchor="center")
        self.trv.heading("이름", text="이름", anchor="center")
        self.trv.column("#3", width=150, anchor="center")
        self.trv.heading("ID", text="ID", anchor="center")
        self.trv.grid(row=3, column=0)