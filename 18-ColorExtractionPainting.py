from turtle import Turtle, Screen
import random
import turtle as t
# import colorgram

# colors = colorgram.extract('hirst.jpg', 88)

# colors_rgb = []

# for i in range(len(colors)):
#     colors_rgb.append((colors[i].rgb.r, colors[i].rgb.g, colors[i].rgb.b))

# print(colors_rgb)

color_list = [(212, 3, 33), (195, 183, 5), (219, 3, 1), (225, 157, 69), (246, 215, 29), (197, 87, 22), (247, 215, 1), (62, 46, 131), (21, 99, 162), (75, 19, 57), (7, 198, 149), (240, 61, 139), (90, 181, 213), (131, 216, 236), (180, 42, 94), (8, 206, 222), (40, 44, 69), (94, 35, 18), (32, 154, 80), (218, 127, 180), (80, 196, 124), (248, 152, 180), (243, 87, 18), (114, 81, 2), (147, 184, 245), (51, 114, 213), (35, 58, 56), (254, 4, 2), (129, 222, 205), (237, 169, 159), (254, 3, 10), (11, 90, 107), (2, 246, 225), (37, 80, 73)]

t.colormode(255)
screen = Screen()
tim = Turtle()
tim.color('red', 'black')
tim.pensize(10)
tim.speed("fast")
tim.ht()

for j in range(10):
    tim.penup()
    tim.goto(-200, -200 + j*50)
    for i in range(10):
        tim.pencolor(random.choice(color_list))
        tim.dot()
        tim.fd(50)
    
screen.exitonclick()