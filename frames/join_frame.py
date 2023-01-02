import tkinter
from tkinter import ttk
from repo.student_repo import student_repo

class join_frame:
    def __init__(self,window):
        self.s_repo = student_repo()
        self.frame = tkinter.Frame(window)
        self.frame.grid(row=1, column=0, sticky="nsew")
        self.label_id = tkinter.Label(window, text="아이디",width=10)
        self.label_pw = tkinter.Label(window, text="패스워드",width=10)

        self.entry_id = tkinter.Entry(window, text="아이디",width=15)
        self.entry_pw = tkinter.Entry(window, text="패스워드",width=15)

        ttk.Label(self.frame, text="이름 : ")\
        .grid(row=1, column=0, padx=10, pady=10)
        ttk.Label(self.frame, text="ID : ")\
        .grid(row=2, column=0, padx=10, pady=10)
        ttk.Label(self.frame, text="비밀번호 : ")\
        .grid(row=3, column=0, padx=10, pady=10)
        ttk.Label(self.frame, text="비밀번호 확인 : ")\
        .grid(row=4, column=0, padx=10, pady=10)

        ent_name = ttk.Entry(self.frame, textvariable='name')
        ent_name.grid(row=1, column=1, padx=10, pady=10)

        ent_id = ttk.Entry(self.frame, textvariable='id')
        ent_id.grid(row=2, column=1, padx=10, pady=10)

        ent_pw = ttk.Entry(self.frame, textvariable='pw', show="*")
        ent_pw.grid(row=3, column=1, padx=10, pady=10)

        ent_repw = ttk.Entry(self.frame, textvariable='repw', show="*")
        ent_repw.grid(row=4, column=1, padx=10, pady=10)

        ttk.Button(self.frame, text="등록", width=10, command=lambda:self.s_repo.submit(ent_id.get(),ent_pw.get()))\
        .grid(row=5, column=0, padx=10, pady=10)