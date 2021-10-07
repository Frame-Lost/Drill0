import turtle
import random

# 그림그리기
# 직선 원 타원 제외


def stop():
    turtle.bye()


def prepare_turtle_canvas():
    turtle.setup(1024, 768)
    turtle.bgcolor(0.2, 0.2, 0.2)
    turtle.penup()
    turtle.hideturtle()
    turtle.shape('arrow')
    turtle.shapesize(2)
    turtle.pensize(5)
    turtle.color(1, 0, 0)
    turtle.speed(100)
    turtle.goto(-500, 0)
    turtle.pendown()
    turtle.goto(480, 0)
    turtle.stamp()
    turtle.penup()
    turtle.goto(0, -360)
    turtle.pendown()
    turtle.goto(0, 360)
    turtle.setheading(90)
    turtle.stamp()
    turtle.penup()
    turtle.home()

    turtle.shape('circle')
    turtle.pensize(1)
    turtle.color(0, 0, 0)
    turtle.speed(50)

    turtle.onkey(stop, 'Escape')
    turtle.listen()


def draw_big_point(p):
    turtle.goto(p)
    turtle.color(0.8, 0.9, 0)
    turtle.dot(15)
    turtle.write('     '+str(p))


def draw_point(p):
    turtle.goto(p)
    turtle.dot(5, random.random(), random.random(), random.random())


def draw_line_basic(p1, p2):
    draw_big_point(p1)
    draw_big_point(p2)
    x1, y1 = p1
    x2, y2 = p2
    # y = ax + b ==> b = y - a * x
    a = (y2-y1)/(x2-x1)
    b = y1 - a * x1

    for x in range(x1, x2+1, 10):
        y = a * x + b
        draw_point((x, y))

    draw_point(p2)

    pass


def draw_star():
    global p1, p2, p3, p4, p5
    draw_line_basic(p1, p4)
    draw_line_basic(p4, p5)
    draw_line_basic(p3, p2)
    draw_line_basic(p1, p2)
    draw_line_basic(p3, p5)


def draw_pentagon():
    global p1, p2, p3, p4, p5
    draw_line_basic(p3, p4)
    draw_line_basic(p3, p1)
    draw_line_basic(p4, p2)
    draw_line_basic(p1, p5)
    draw_line_basic(p5, p2)


def draw_inverted_triangle():
    global p6, p7, p8
    draw_line_basic(p6, p7)
    draw_line_basic(p6, p8)
    draw_line_basic(p7, p8)
    pass


def draw_line(p1, p2):
    # fill here
    pass


prepare_turtle_canvas()
p1 = (-70, -20)
p2 = 100, 120
p3 = -100, 120
p4 = 0, 190
p5 = 70, -20
p6 = -115, 190
p7 = 0, -1190/3+50
p8 = 115, 190


draw_star()
draw_pentagon()
draw_inverted_triangle()

turtle.done()