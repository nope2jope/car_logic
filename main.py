from turtle import Turtle, Screen
import random

screen = Screen()
turtle = Turtle()

screen.setup(width=600, height=600)

turtle.ht()
turtle.pu()
turtle.seth(180)
turtle.goto(300, 0)
turtle.st()

turtle_list = []


def make_turt():

    x_coord = 300
    y_coord = random.randint(-235, 235)
    turt = Turtle()
    turt.ht()
    turt.shape("square")
    turt.shapesize(stretch_wid=1, stretch_len=5)
    turt.pu()
    turt.seth(180)
    turt.setposition(x_coord, y_coord)
    turt.st()
    turtle_list.append(turt)

gameon = True


while gameon:
    for turtle in turtle_list:
        turtle.forward(50)
    make_turt()

screen.exitonclick()