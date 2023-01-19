from turtle import Turtle, Screen
import random
import turtle as t

t.colormode(255)
screen = Screen()
screen.bgcolor("wheat")

tim = Turtle()
tim.shape("turtle")
# tim.shapesize(3, 3, 2)
tim.color('red', 'black')
tim.pensize(3)
tim.speed("fastest")


def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)

def move_forwards():
    tim.fd(10)

def move_backwards():
    tim.bk(10)

def turn_right():
    tim.rt(10)

def turn_left():
    tim.lt(10)

def clear():
    screen.resetscreen()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="c", fun=clear)

screen.exitonclick()