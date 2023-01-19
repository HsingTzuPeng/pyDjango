import freegames
import turtle
import random

答案x,答案y = 0,0 # 全域變數
色彩字典 = {1:('red','red3'),2:('SeaGreen1','SeaGreen3'),3:('SteelBlue1','SteelBlue3')}
畫面編號 = 1

def func(x,y) :

    global 畫面編號
    if 答案x < x < 答案x+100 and 答案y < y < 答案y+100 :
        print('答對了')
        畫面編號 += 1
        func1()
    return None

def func1() :

    global 答案x,答案y
    if 畫面編號 < 4 :
        答案x, 答案y = 畫面繪製(色彩字典[畫面編號])
        print(答案x, 答案y)
    else :
        turtle.exitonclick()

def 畫面繪製( tuple1 ):

    a = random.randint(1,16)
    color1 = tuple1[0]
    color2 = tuple1[1]

    num = 1
    for y in range(4):
        for x in range(4):
            if a != num :
                freegames.square( -275 + x * 150, 175 - y * 150, 100, color1)
            else :
                freegames.square( -275 + x * 150, 175 - y * 150, 100, color2)
                ans_x = -275 + x * 150
                ans_y = 175 - y * 150
            num += 1

    return (ans_x,ans_y)


screen = turtle.Screen()
screen.listen()
screen.onclick(func)
screen.setup(600, 600, 400, 0)

turtle.hideturtle()
turtle.tracer(False)
func1()