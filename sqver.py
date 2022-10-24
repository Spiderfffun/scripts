import turtle as t
t.shape("arrow")
t.bgcolor("red")
t.color("blue")
t.pensize(3)
t.speed(500)
t.right(180)
t.penup()
t.forward(850)
t.right(90)
t.forward(500)
t.right(90)
t.pendown()
for i in range(90):
        for j in range(70):
            for k in range(4):
                t.forward(25)
                t.right(90)
            t.penup()
            t.forward(25)
            t.pendown()
        t.right(90)
        t.forward(50)
        t.right(90)
        for j in range(70):
            for k in range(4):
                t.forward(25)
                t.right(90)
            t.penup()
            t.forward(25)
            t.pendown()
        t.right(180)
