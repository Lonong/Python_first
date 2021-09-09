import turtle
import time

# 实现清屏
def clear_screen():
    turtle.penup()             #画笔抬起
    turtle.goto(0,0)        #定位到（0，0）
    turtle.color('white')
    turtle.pensize(800)         #画笔粗细
    turtle.pendown()           #画笔落下
    turtle.setheading(0)        #设置朝向
    turtle.fd(300)       #前进
    turtle.bk(600)      #后退

# 初始化海龟的位置
def go_start(x, y, state):
    turtle.pendown() if state else turtle.penup()
    turtle.goto(x, y)

#画线，state为真时海龟回到原点，为假时不回到原来的出发点
def draw_line(length, angle, state):
    turtle.pensize(1)
    turtle.pendown()
    turtle.setheading(angle)
    turtle.fd(length)
    turtle.bk(length) if state else turtle.penup()
    turtle.penup()

# 画出发射爱心的小人
def draw_people(x, y):
    turtle.speed(100)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.pensize(2)
    turtle.color('black')
    turtle.setheading(0)
    turtle.circle(35, 360)
    turtle.penup()
    turtle.pensize(3)
    turtle.setheading(90)
    turtle.fd(45)
    turtle.setheading(180)
    turtle.fd(20)
    turtle.setheading(0)
    turtle.fd(35)
    turtle.pendown()
    turtle.circle(4, 360)
    turtle.penup()
    turtle.goto(x, y)
    turtle.pensize(2)
    turtle.setheading(0)
    turtle.fd(20)
    turtle.setheading(90)
    turtle.fd(20)
    turtle.setheading(-90)
    turtle.pendown()
    turtle.circle(5, 180)
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(-90)
    turtle.pendown()
    turtle.fd(20)
    turtle.setheading(0)
    turtle.fd(35)
    turtle.setheading(60)
    turtle.fd(10)
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(-90)
    turtle.pendown()
    turtle.fd(40)
    turtle.setheading(0)
    turtle.fd(35)
    turtle.setheading(-60)
    turtle.fd(10)
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(-90)
    turtle.pendown()
    turtle.fd(60)
    turtle.setheading(-135)
    turtle.fd(60)
    turtle.bk(60)
    turtle.setheading(-45)
    turtle.fd(30)
    turtle.setheading(-135)
    turtle.fd(35)
    turtle.penup()


# 画爱心
def draw_heart(size):
    turtle.speed(100)
    turtle.color('red', 'pink')
    turtle.pensize(2)
    turtle.pendown()
    turtle.setheading(150)
    turtle.begin_fill()
    turtle.fd(size)
    turtle.circle(size * -3.745, 45)
    turtle.circle(size * -1.431, 165)
    turtle.left(120)
    turtle.circle(size * -1.431, 165)
    turtle.circle(size * -3.745, 45)
    turtle.fd(size)
    turtle.end_fill()

# 画箭羽
def draw_feather(size):
    turtle.speed(100)
    angle = 30  # 箭的倾角
    feather_num = size // 6    # 羽毛的数量
    feather_length = size // 3     # 羽毛的长度
    feather_gap = size // 10     # 羽毛的间隔
    for i in range(feather_num):
        draw_line(feather_gap, angle + 180, False)  # 箭柄，不折返
        draw_line(feather_length, angle + 145, True)  # 羽翼，要折返
    draw_line(feather_length, angle + 145, False)
    draw_line(feather_num * feather_gap, angle, False)
    draw_line(feather_length, angle + 145 + 180, False)
    for i in range(feather_num):
        draw_line(feather_gap, angle + 180, False)   # 箭柄，不折返
        draw_line(feather_length, angle - 145, True)    # 羽翼，要折返
    draw_line(feather_length, angle - 145, False)
    draw_line(feather_num * feather_gap, angle, False)
    draw_line(feather_length, angle - 145 + 180, False)

# 画一箭穿心,最后箭的头没有画出来，用海龟来代替
def arrow_heart(x, y, size):
    turtle.speed(100)
    go_start(x, y, False)
    draw_heart(size * 1.15)
    turtle.setheading(-150)
    turtle.penup()
    turtle.fd(size * 2.2)
    draw_heart(size)
    turtle.penup()
    turtle.setheading(150)
    turtle.fd(size * 2.2)
    turtle.color('black')
    draw_feather(size)
    turtle.pensize(4)
    turtle.setheading(30)
    turtle.pendown()
    turtle.fd(size * 2)
    turtle.penup()
    turtle.setheading(29)
    turtle.fd(size * 5.7)
    turtle.color('black')
    turtle.pensize(4)
    turtle.pendown()
    turtle.fd(size * 1.2)

#显示倒数3,2,1
def draw_0(i):
    turtle.speed(30)
    turtle.penup()
    turtle.hideturtle()  # 隐藏箭头显示
    turtle.goto(-50, -100)
    turtle.color('red')
    write = turtle.write(i, font=('宋体', 200, 'normal'))
    time.sleep(1)

# 显示文字
def draw_1():
    turtle.penup()
    turtle.hideturtle()    #隐藏箭头显示
    turtle.goto(-250, 0)
    turtle.color('red')
    write = turtle.write('臭猪猪，接招', font=('宋体', 60, 'normal'))
    time.sleep(2)

# 显示发射爱心的小人儿
def draw_2():
    turtle.speed(3)
    draw_people(-250, 20)
    turtle.penup()
    turtle.goto(-150, -30)
    draw_heart(14)
    turtle.penup()
    turtle.goto(-20, -60)
    draw_heart(25)
    turtle.penup()
    turtle.goto(205, -100)
    draw_heart(43)
    turtle.hideturtle()
    time.sleep(2)

def draw_3():
    turtle.speed(30)
    turtle.penup()
    turtle.hideturtle()  # 隐藏箭头显示
    turtle.goto(-220, 50)
    turtle.color('red')
    write = turtle.write('💕不离', font=('宋体', 60, 'normal'))
    turtle.penup()
    turtle.goto(0, -50)
    write = turtle.write('不弃💕', font=('宋体', 60, 'normal'))
    time.sleep(2)


# 显示一箭穿心
def draw_4():
    turtle.speed(10)
    turtle.penup()
    turtle.goto(-210, -200)
    turtle.color('blue')
    turtle.pendown()
    turtle.write('YRB      CQZ', font=('wisdom', 50, 'normal'))
    turtle.speed(1)
    turtle.penup()
    turtle.color("red")
    turtle.goto(-31, -200)
    turtle.write('❤',font=('wisdom', 50, 'normal'))
    arrow_heart(20, -60, 51)
    turtle.showturtle()


number=[3,2,1]    #储存显示界面倒数数字1,2,3

if __name__ == '__main__':
    turtle.setup(900, 500)     #调画布的尺寸
    for i in number:
        draw_0(i)
        clear_screen()
    draw_1()
    clear_screen()
    draw_2()
    clear_screen()
    draw_3()
    clear_screen()
    draw_4()
    turtle.done()
