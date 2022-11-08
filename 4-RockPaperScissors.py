import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

options = [rock, paper, scissors]
computer_choice = str(random.choice(options))
decision = "draw"

choice = input(
    "Welcome to Rock, Paper, Scissors! \nYou know the rules, let's play a game. \nWhat do you choose? Type r for rock, p for paper, and s for scissors.\n"
)
if choice == "r":
    choice = rock
    if computer_choice == paper:
        decision = "lose"
    elif computer_choice == scissors:
        decision = "win"
    else:
        decision = "draw"

elif choice == "p":
    choice = paper
    if computer_choice == paper:
        decision = "draw"
    elif computer_choice == scissors:
        decision = "lose"
    else:
        decision = "win"

elif choice == 's':
    choice = scissors
    if computer_choice == paper:
        decision = "win"
    elif computer_choice == scissors:
        decision = "draw"
    else:
        decision = "lose"
else:
    print("You did not type in a valid option. Please restart!")
    quit()

print(
    f"You chose {choice} \nand the computer chose {computer_choice} \nSo you {decision}"
)
