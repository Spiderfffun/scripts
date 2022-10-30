#originally named math.py for no reason at all
import turtle
turtle.pensize(2)
turtle.hideturtle()
turtle.penup()
#turtle.rt(90)
#turtle.fd(450)
#turtle.lt(90)
turtle.pendown()
n = 2
turtle.speed(0)
while True:
    n = n + 1
    Sn = (n - 2)*180
    angle = 180 - Sn/n
    for i in range(4):
        for i in range(n):
            turtle.fd(50)
            turtle.lt(angle)
        turtle.fd(50)
        turtle.rt(90) 
        
