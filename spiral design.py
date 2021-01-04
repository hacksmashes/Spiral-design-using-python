import turtle

colors=["red","green","orange","purple","yellow","blue"]
t=turtle.Pen()
t.speed(50)
turtle.bgcolor("black")
for i in range(1000):
    t.pencolor(colors[i%6])
    t.width(i/100+2)
    t.forward(i)
    t.left(59)

turtle.done()