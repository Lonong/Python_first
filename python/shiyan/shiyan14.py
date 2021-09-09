# coding=utf-8


import random
import tkinter

def main():
    win = tkinter.Tk()
    win.title('摇骰子')
    win.geometry("500x200")
    w = tkinter.Button(win,text ="点我摇骰子",command =shaizi)
    w.pack(expand="yes",ipadx=35,ipady=5)# 将小部件放置到主窗口中



    win.mainloop()  # 进入消息循环

def shaizi():
    face = random.randint(1, 6)
    if face == 1:
        result = '唱首歌'
    elif face == 2:
        result = '跳个舞'
    elif face == 3:
        result = '学狗叫'
    elif face == 4:
        result = '做俯卧撑'
    elif face == 5:
        result = '念绕口令'
    else:
        result = '讲冷笑话'

    print(result)
    # wi = tkinter.Tk()
    # wi.title('摇骰子')
    # wi.geometry("500x200")
    # l = wi.Label(wi,textvariable=result, bg='green', font=('Arial', 12), width=30, height=2)
    # l.pack()
    # wi.mainloop()  # 进入消息循环






if __name__ == '__main__':
    main()
