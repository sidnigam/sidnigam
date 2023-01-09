from prettytable import PrettyTable

x = PrettyTable()
x.field_names = ["Pokemon Name", "Type"]
x.add_rows(
    [
        ["Pikachu", "Electric" ],
        ["Squirtle", "Water" ],
        ["Charmander", "Fire" ],
        ["Bulbasaur", "Grass" ],
    ]
)
x.align = "l"       # attribute
print(x)


# from turtle import Turtle, Screen

# timmy = Turtle()        # object
# timmy.color("coral")    # attribute
# timmy.shape("turtle")   # attribute

# steps = 0

# while steps < 10:
#     timmy.fd(50)        # method
#     timmy.lt(36)        # method
#     timmy.fd(50)
#     steps += 1

# while steps > 0:
#     timmy.fd(50)
#     timmy.rt(36)
#     timmy.fd(50)
#     steps -= 1

# my_screen = Screen()

# # print(my_screen.canvheight)     # screen is object, canvheight is attribute
# my_screen.exitonclick()


