def ㅇ(x, y, r, t):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.circle(r)

def ㅠ(x, y, d, t):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.forward(d)

    t.right(90)
    t.penup()
    t.goto(x + 50, y)
    t.pendown()
    t.forward(d / 2)
    
    t.penup()
    t.goto(x + 150, y)
    t.pendown()
    t.forward(d / 2)
    
def ㅅ(x, y, d, t):
    t.penup()
    t.goto(x, y)
    t.right(30)
    t.pendown()
    t.forward(d)
    
    t.goto(x, y)
    t.left(60)
    t.pendown()
    t.forward(d)

def ㅣ(x, y, a, d, t):
    t.penup() 
    t.goto(x, y)
    t.right(a)
    t.pendown()
    t.forward(d)
        
import turtle as t

ㅇ(-350, 50, 50, t)
ㅠ(-450, -10, 200, t)

ㅅ(-50, 130, 120, t)
ㅣ(60, 150, 30, 80, t)
t.right(90)
t.forward(50)
t.backward(50)
t.left(90)
ㅣ(60, 70, 0, 80, t)

ㅣ(-70, -40, -90, 110, t)
ㅣ(40, -40, 90, 80, t)

ㅅ(350, 130, 120, t)
ㅣ(280, 130, -60, 140, t)

ㅣ(450, 150, 90, 150, t)

ㅣ(330, -30, 0, 80, t)
ㅣ(330, -110, -90, 120, t)

t.exitonclick()