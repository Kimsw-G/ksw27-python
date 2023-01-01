import tkinter

window = tkinter.Tk()

window.title('login')
window.geometry("640x400+100+100")
window.resizable(False,False)

label=tkinter.Label(window, text="0", width=10, height=5, fg="red", relief="solid")
label.pack()

cnt=0

def countUP():
    global cnt
    cnt += 1
    label.config(text=str(cnt))

button = tkinter.Button(window,overrelief='solid',width=15,command=countUP,repeatdelay=1000,repeatinterval=100)
button.pack()

def calc(event):
    label.config(text="결과="+str(eeval(entry.get())))

entry = tkinter.Entry(window)
entry.bind("<Return>",calc)
entry.pack()


window.mainloop()