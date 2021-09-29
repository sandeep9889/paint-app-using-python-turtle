import turtle
colors = ['blue' , 'red' , 'blue' , 'red']
t = turtle.pen()
t.speed(9)
t.pensize(0.1)
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x/100 + 1)
    t.forward(x)
    t.left(59)
