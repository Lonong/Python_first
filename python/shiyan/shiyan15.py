# coding=utf-8
from tkinter import *

'''
1、设置两个frame类型按钮，当点击Button按钮触发command命令。
2、command命令指向一个事件，改变页面显示的内容。
'''

root = Tk()
# 1、设置两个Frame窗口。一个容器窗口部件。帧可以有边框和背景，当创建一个应用程序或dialog(对话）版面时，帧被用来组织其它的窗口部件。
frame1 = Frame(root)
frame2 = Frame(root)
var = StringVar()
var.set('您不是会员不能下载VIP资源\n前先注册会员再来下载资源')
# 2、设置第一个Label显示文本内容。
textLabel = Label(frame1,
                  textvariable=var,  # 与按钮相关的Tk变量（通常是一个字符串变量）。如果这个变量的值改变，那么按钮上的文本相应更新。
                  justify=LEFT,  # 定义多行文本如何对齐。可取值有：LEFT, RIGHT, 或 CENTER。
                  )
textLabel.pack(side=RIGHT)  # 按扭停靠在窗口的哪个位置left: 左,top: 上,right: 右,botton: 下
# 3、设置第二个Label显示图片信息。
photo = PhotoImage(file="xiaoxiang.gif")  # PhotoImage()方法只支持gif格式的图片。
imgLabel = Label(root, image=photo)
imgLabel.pack(side=LEFT)


def callback():
    var.set('你的身份验证失败，你不是会员')

    # 4、设置一个Button按钮触发callback方法。


theButton = Button(frame2, text='我已注册会员', command=callback)
theButton.pack()
# 5、设置两个frame窗口的大小
frame1.pack(padx=10, pady=10)
frame2.pack(padx=10, pady=10)
mainloop()