import turtle

"""绘制矩形"""
x, y = -270, -180
width, height = 540, 360
turtle.hideturtle()  # 隐藏画笔形状
turtle.speed(10)  # 画笔移动速度
turtle.up()  # 提笔
turtle.goto(x, y)
turtle.down()   #放笔
turtle.color('white','red')  # 线条色和填充色
turtle.begin_fill()    # 开始填充


for i in range(2):  # 旋转两个90度
    turtle.forward(width)
    turtle.left(90)
    turtle.forward(height)
    turtle.left(90)
turtle.end_fill()

# 画心心函数
def drow_star (lig, x, y):
    turtle.up()
    turtle.goto(x,y)
    turtle.down()
    turtle.speed(100)
    turtle.begin_fill()
    turtle.pensize(1)
    turtle.width(0)
    turtle.pencolor("yellow")
    turtle.fillcolor("yellow")
    for _ in range(5):
        turtle.forward(lig)   #线条长度
        turtle.right(144)    #转折角度
    turtle.end_fill()





def main():
    # 画大鑫鑫
    x,y=-260, 100
    lig = 100
    drow_star(lig,x,y)
    # 画小心心
    x_poses, y_poses = [-145, -125,-130, -150], [140, 100, 60, 20]
    lig = 25
    for x, y in zip(x_poses, y_poses):
        drow_star(lig, x, y)

    turtle.up()
    turtle.goto(-100, -250)
    turtle.down()
    turtle.color('red')
    turtle.write("print(China）", font=("宋体", 18, "normal"))
    turtle.mainloop()  # 展示窗口




if __name__ == '__main__':
    main()







