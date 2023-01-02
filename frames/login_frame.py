import tkinter
from tkinter import ttk
from repo.student_repo import student_repo

class login_frame:
    def __init__(self,window):
        self.s_repo = student_repo()
        self.frame = tkinter.Frame(window)
        self.frame.grid(row=1, column=0, sticky="nsew")
        ttk.Label(self.frame, text="ID : ")\
        .grid(row=0, column=0, padx=10, pady=10)
        ttk.Label(self.frame, text="Password : ")\
        .grid(row=1, column=0, padx=10, pady=10)
        ent_id = ttk.Entry(self.frame, textvariable=id)
        ent_id.grid(row=0, column=1, padx=10, pady=10)

        ent_pw = ttk.Entry(self.frame, textvariable='pw', show="*")
        ent_pw.grid(row=1, column=1, padx=10, pady=10)

        self.button = ttk.Button(self.frame,text="로그인",width=15,command=lambda:self.s_repo.login(ent_id.get(),ent_pw.get()))
        self.button.grid()