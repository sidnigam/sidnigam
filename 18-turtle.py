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

# colors = ["red", "green", "orange", "black", "blue", "magenta"]
turns = [90, 180, 270, 360]

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r, g, b)

for i in range(37):
    tim.pencolor(random_color())
    # for j in range(i):
    tim.circle(100)
    tim.fd(10)
    tim.stamp()
    tim.bk(5)
    tim.rt(10)
    tim.fd(random.choice(range(10,50)))

    
tim.ht()
screen.exitonclick()
