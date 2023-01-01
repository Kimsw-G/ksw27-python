from myModules import MyDBCP
import tkinter


mydbcp = MyDBCP.MyDBCP()

window = tkinter.Tk()

window.title('login')
window.geometry("640x400+100+100")
window.resizable(False,False)

## 테스트 
# test_label = tkinter.Label(window,text="0", width=10, height=5, fg="red", relief="solid")
# test_label.pack(side='bottom')
# def login(id,pw):
#     mt = id+pw
#     print(mt)
#     test_label.config(text=mt)

label_id = tkinter.Label(window, text="아이디",width=10)
label_pw = tkinter.Label(window, text="패스워드",width=10)

entry_id = tkinter.Entry(window, text="아이디",width=15)
entry_pw = tkinter.Entry(window, text="패스워드",width=15)

button_login = tkinter.Button(window, text="login",width=15,command=lambda:mydbcp.login(entry_id.get(), entry_pw.get()),repeatdelay=1000,repeatinterval=100)

label_id.place(x=30,y=20)
entry_id.place(x=130,y=20)
label_pw.place(x=30,y=40)
entry_pw.place(x=130,y=40)
button_login.place(x=80,y=80)

window.mainloop()

