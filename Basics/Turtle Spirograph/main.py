import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
testoasa = Turtle()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

testoasa.shape("turtle")
testoasa.speed(0)
testoasa.color(random_color())


def spirograph(degree):
    for i in range(int(360 / degree)):
        testoasa.circle(150)
        testoasa.setheading(testoasa.heading() + degree)
        testoasa.color(random_color())

spirograph(2)




screen = Screen()
screen.exitonclick()