#makes the turtle
import turtle
#this ma
t = turtle.Turtle()
s = turtle.Screen()
#changes the turtle setting
turtle.speed(0)
run = 0
runtimes = 1 
design = 0
designamount = 4
#draws the dragon
while run < runtimes :
    #makes the body
    t.penup()
    t.goto(-100,0)
    t.pendown()
    t.color("red")
    t.begin_fill()
    t.forward(400)
    t.right(90)
    t.forward(150)
    t.right(90)
    t.forward(400)
    t.right(90)
    t.forward(150)
    #draws the head
    t.right(270)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(100)
    t.end_fill()
    #draws the legs
    t.penup()
    t.goto(-20,-145)
    t.pendown()
    t.color("red")
    t.begin_fill()
    t.forward(90)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(90)
    t.right(90)
    t.forward(30)
    t.end_fill()
    t.penup()
    t.goto(40,-145)
    t.pendown()
    t.color("red")
    t.begin_fill()
    t.right(90)
    t.forward(90)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(90)
    t.right(90)
    t.forward(30)
    t.end_fill()
    t.penup()
    t.goto(180,-145)
    t.pendown()
    t.color("red")
    t.begin_fill()
    t.right(90)
    t.forward(90)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(90)
    t.right(90)
    t.forward(30)
    t.end_fill()
    t.penup()
    t.goto(240,-145)
    t.pendown()
    t.color("red")
    t.begin_fill()
    t.right(90)
    t.forward(90)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(90)
    t.right(90)
    t.forward(30)
    t.end_fill()
    t.penup()
    t.goto(-175,60)
    t.pendown()
    #draws the eyes
    t.color("white")
    t.begin_fill()
    t.circle(15)
    t.end_fill()
    t.penup()
    t.goto(-130,60)
    t.color("white")
    t.begin_fill()
    t.circle(15)
    t.end_fill()
    t.penup()
    t.goto(-175,65)
    t.pendown()
    t.color("black")
    t.begin_fill()
    t.circle(8)
    t.end_fill()
    t.penup()
    t.goto(-130,65)
    t.pendown()
    t.color("black")
    t.begin_fill()
    t.circle(8)
    t.end_fill()
    #draw mouth
    t.penup()
    t.goto(-190,30)
    t.pendown()
    t.color("blue")
    t.width(5)
    t.begin_fill()
    t.forward(80)
    t.end_fill()
    #draws tail
    t.penup()
    t.goto(295,0)
    t.pendown()
    t.color("purple")
    t.begin_fill()
    t.left(55)
    t.forward(150)
    t.right(100)
    t.forward(60)
    t.right(100)
    t.forward(150)
    t.end_fill()
    t.penup()
    t.goto(50,-75)
    run += 1

while design < designamount:
    t.color("blue")
    t.right(180)
    t.pendown()
    t.forward(40)
    t.right(90)
    t.forward(40)
    t.left(45)
    design += 1



    

#keeps turtle screen from disapering
s.exitonclick()