import turtle
turtle.penup()
turtle.goto(-200,200)
turtle.pendown()
count=5
length=500
while(count>0):
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    count -= 1
    length -= 100

turtle.penup()
turtle.goto(300,-300)
turtle.pendown()
turtle.right(180)

count = 4
length = 400
while(count>0):
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    turtle.forward(length)
    turtle.right(90)
    count -= 1
    length -= 100


turtle.exitonclick()
