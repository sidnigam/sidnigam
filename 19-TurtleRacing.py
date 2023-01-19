from turtle import Turtle, Screen
import random
import turtle as t
       
t.colormode(255)
screen = Screen()
screen.setup(width = 500, height = 400)
screen.bgcolor("wheat")
user_bet = screen.textinput(title = "Make your bet", prompt = "which turtle will win? Enter a color")

colors = ["violet", "indigo", "blue", "green", "yellow", "orange", "red"]
y_location = range(-150,200,50)
turtles = []

for selected_turtle in range(7):
    new_turtle = Turtle(shape = "turtle")
    new_turtle.penup()
    new_turtle.color(colors[selected_turtle])
    new_turtle.goto(x = -200, y = y_location[selected_turtle])
    turtles.append(new_turtle)

is_race_on = False
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False    
            winner = turtle.pencolor()
            if winner == user_bet:
                print(f"You've won! The {winner} turtle is the winner!")
            else: 
                print(f"You've lost! The {winner} turtle is the winner!")
        rand_distance = random.randint(0, 10)
        turtle.fd(rand_distance)

screen.exitonclick()