import tkinter
from repo.student_repo import student_repo
from frames.list_frame import list_frame
from frames.login_frame import login_frame
from frames.join_frame import join_frame

def openFrame(frame):
    frame.tkraise()

s_repo = student_repo()

window = tkinter.Tk()
s_frame = list_frame(window)
l_frame = login_frame(window)
j_frame = join_frame(window)

login_button = tkinter.Button(window,text='로그인',width=15,command=lambda:[openFrame(l_frame.frame)])
list_button = tkinter.Button(window,text='목록',width=15,command=lambda:[openFrame(s_frame.frame)])
join_button = tkinter.Button(window,text='회원가입',width=15,command=lambda:[openFrame(j_frame.frame)])

login_button.grid()
list_button.grid()
join_button.grid()

window.title('student')
window.geometry("640x400+100+100")
window.resizable(False,False)



window.mainloop()