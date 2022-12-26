# Initialization and constant variables
import random

welcome = """
     |\_/|                  
     | @ @   Woof! 
     |   <>              _  
     |  _/\------____ ((| |))
     |               `--' |   
 ____|_       ___|   |___.' 
/_/_____/____/_______|

Welcome to the number guessing game! Woof!

I'll select a number from 1 - 100 randomly, and you have to guess it. Easy right?
Alright let's begin. Ruff ruff! 

What mode do you want? 
"""

def guess_checker():
    if guess > number:
        print("Too high.")
        return guesses - 1
    elif guess < number:
        print("Too low.")
        return guesses - 1
    elif guess == number:
        print(f"You got it! The answer was {guess}")
        return guesses - guesses

number = random.randint(1,100)
print(welcome)

mode = input("Type 'easy' (10 guesses) or 'hard' (5 guesses): ")
if mode == 'easy': guesses = 10
else: guesses = 5

while not guesses == 0:
    guess = int(input("Make a guess: "))
    guesses = guess_checker()
    if guesses != 0:
        print(f"You have {guesses} attempts remaining to guess the number.\nGuess again.")
