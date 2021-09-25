import turtle

win = turtle.Screen()
win.setup(900,600)
win.title("paint apk by sandeep")

# ribbon
rib = turtle.Turtle()
rib.hideturtle()
rib.color('thistle')
rib.shape('square')
rib.shapesize(2,46) 
rib.penup() # pens ip
rib.goto(0,280) #pens goto this coordinate
rib.showturtle() #here it can be shown  the implement

# brush
bru = turtle.Turtle()
bru.hideturtle() #it can hide moving turtle
bru.color('crimson')
bru.penup()
bru.shape('square')
bru.shapesize(2,4)
bru.goto(-420,280)
bru.showturtle()

# brush writer
bru1 = turtle.Turtle()
bru1.hideturtle()
bru1.color('white')
bru1.penup()
bru1.shape('square')
bru1.shapesize(1)
bru1.goto(-420,280)
bru1.pendown()
bru1.write('Brush' , align = 'center' , font = ('courier' , 12 , 'bold')) #here  i have alling at the center
bru1.goto(-420,270)
bru1.showturtle()

# pensize
p = turtle.Turtle()
p.hideturtle()
p.color('crimson')
p.penup()
p.shape('square')
p.shapesize(1,1)
p.goto(-330,290)
p.showturtle()
p1= turtle.Turtle()
#from here  we can a build a size on crimson colour ribbion
p1.hideturtle()
p1.penup()
p1.goto(-330,285)
p1.pendown()
p1.shape('square')
p1.shapesize(0.3)
p1.color('white')
p1.write('6')
p1.penup()
p1.goto(p1.xcor() , p1.ycor() - 2) #usibox k andar neeche ajayega
p1.showturtle()

p22 = turtle.Turtle()
p22.hideturtle()
p22.color('crimson')
p22.penup()
p22.shape('square')
p22.shapesize(1,1)
p22.goto(-310,290)
p22.showturtle()
p2= turtle.Turtle()
p2.hideturtle()
p2.penup()
p2.goto(-310,285)
p2.pendown()
p2.shape('square')
p2.shapesize(0.3)
p2.color('white')
p2.write('8')
p2.penup()
p2.goto(p2.xcor() , p2.ycor() - 2)
p2.showturtle()

p33 = turtle.Turtle()
p33.hideturtle()
p33.color('crimson')
p33.penup()
p33.shape('square')
p33.shapesize(1,1)
p33.goto(-290,290)
p33.showturtle()
p3= turtle.Turtle()
p3.hideturtle()
p3.penup()
p3.goto(-290,285)
p3.pendown()
p3.shape('square')
p3.shapesize(0.3)
p3.color('white')
p3.write('10')
p3.penup()
p3.goto(p3.xcor() , p3.ycor() - 2)
p3.showturtle()

p44 = turtle.Turtle()
p44.hideturtle()
p44.color('crimson')
p44.penup()
p44.shape('square')
p44.shapesize(1,1)
p44.goto(-270,290)
p44.showturtle()
p4= turtle.Turtle()
p4.hideturtle()
p4.penup()
p4.goto(-270,285)
p4.pendown()
p4.shape('square')
p4.shapesize(0.3)
p4.color('white')
p4.write('12')
p4.penup()
p4.goto(p4.xcor() , p4.ycor() - 2)
p4.showturtle()

p00 = turtle.Turtle()
p00.hideturtle()
p00.color('crimson')
p00.penup()
p00.shape('square')
p00.shapesize(1,1)
p00.goto(-250,290)
p00.showturtle()
p0= turtle.Turtle()
p0.hideturtle()
p0.penup()
p0.goto(-250,285)
p0.pendown()
p0.shape('square')
p0.shapesize(0.3)
p0.color('white')
p0.write('2')
p0.penup()
p0.goto(p0.xcor() , p0.ycor() - 2)
p0.showturtle()

# colors
c1 = turtle.Turtle()
c1.hideturtle()
c1.color('green')
c1.shape('square')
c1.shapesize(1)
c1.penup()
c1.goto(430,270)
c1.showturtle()

c2 = turtle.Turtle()
c2.hideturtle()
c2.color('red')
c2.shape('square')
c2.shapesize(1)
c2.penup()
c2.goto(430,290)
c2.showturtle()

c3 = turtle.Turtle()
c3.hideturtle()
c3.color('black')
c3.shape('square')
c3.shapesize(1)
c3.penup()
c3.goto(410,290)
c3.showturtle()

c4 = turtle.Turtle()
c4.hideturtle()
c4.color('pink')
c4.shape('square')
c4.shapesize(1)
c4.penup()
c4.goto(410,270)
c4.showturtle()

c5 = turtle.Turtle()
c5.hideturtle()
c5.color('blue')
c5.shape('square')
c5.shapesize(1)
c5.penup()
c5.goto(390,290)
c5.showturtle()

c6 = turtle.Turtle()
c6.hideturtle()
c6.color('white')
c6.shape('square')
c6.shapesize(1)
c6.penup()
c6.goto(390,270)
c6.showturtle()

c7 = turtle.Turtle()
c7.hideturtle()
c7.color('yellow')
c7.shape('square')
c7.shapesize(1)
c7.penup()
c7.goto(370,290)
c7.showturtle()

c8 = turtle.Turtle()
c8.hideturtle()
c8.color('orange')
c8.shape('square')
c8.shapesize(1)
c8.penup()
c8.goto(370,270)
c8.showturtle()

# real brush
bruss = turtle.Turtle()
bruss.hideturtle()
bruss.speed(-1)
bruss.shape('square')
bruss.shapesize(1)
bruss.penup()
bruss.goto(bru1.xcor(),bru1.ycor())
bruss.pendown()

def drag(x,y):
    bruss.ondrag(None) #if we dont apply ondrag the comes to it original position 
    bruss.setheading(bruss.towards(x,y))
    bruss.goto(x,y)
    bruss.ondrag(drag)

def select(x,y):
    bruss.showturtle()

def clickgreen(x,y):
    bruss.color('green')

def clickred(x,y):
    bruss.color('red')

def clickpink(x,y):
    bruss.color('pink')

def clickblack(x,y):
    bruss.color('black')

def clickwhite(x,y):
    bruss.color('white')

def clickblue(x,y):
    bruss.color('blue')

def clickyellow(x,y):
    bruss.color('yellow')

def clickorange(x,y):
    bruss.color('orange')

def chgsiz6(x,y):
    bruss.pensize(6)

def chgsiz12(x,y):
    bruss.pensize(8)

def chgsiz18(x,y):
    bruss.pensize(10)

def chgsiz24(x,y):
    bruss.pensize(12)

def chgsiz2(x,y):
    bruss.pensize(2)
    
win.listen()
bru1.onclick(select , 1)
bruss.ondrag(drag , 1)
c1.onclick(clickgreen , 1)
c2.onclick(clickred ,1)
c3.onclick(clickblack ,1)
c4.onclick(clickpink ,1)
c5.onclick(clickblue ,1)
c6.onclick(clickwhite,1)
c7.onclick(clickyellow ,1)
c8.onclick(clickorange ,1)
p1.onclick(chgsiz6 , 1)
p2.onclick(chgsiz12 , 1)
p3.onclick(chgsiz18 , 1)
p4.onclick(chgsiz24 , 1)
p0.onclick(chgsiz2 , 1)

# turtle.mainloop()