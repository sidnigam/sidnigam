#ANCHOR - Put Treasure
# # 🚨 Don't change the code below 👇
# row1 = ["⬜️", "⬜️", "⬜️"]
# row2 = ["⬜️", "⬜️", "⬜️"]
# row3 = ["⬜️", "⬜️", "⬜️"]
# map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
# position = input("Where do you want to put the treasure? ")
# # 🚨 Don't change the code above 👆

# #Write your code below this row 👇

# col = int(([*position])[1])
# row = int(([*position])[0])
# map[col - 1][row - 1] = "X"
# #Write your code above this row 👆

# # 🚨 Don't change the code below 👇
# print(f"{row1}\n{row2}\n{row3}")


#ANCHOR - Lists basics

# Write your code below this line 👇
# Hint: Remember to import the random module first. 🎲

# import random

# random_integer = random.randint(0, 1)
# if random_integer == 0:
#     print('Heads')
# else:
#     print('Tails')

# states = ["Delaware", "Pennsylvania", "Massachusetts"]
# print(states[2])

# states[2] = "Vermont"
# print(states)

# states.extend(["New Hampshire", "NY"])
# print(states)
