# Hangman! 

import random
import hangman_dependencies

chosen_word = random.choice(hangman_dependencies.word_list)
print(hangman_dependencies.logo)
print(f'Pssst, the solution is {chosen_word}.')

lives = 6
display = []
result = ""
for items in chosen_word:
    display.append("_")

while lives > 0:
    counter = 0
    print(display)
    guess = input("Guess a letter: ").lower()
    for letter in chosen_word:
        if letter == guess:
            display[counter] = letter
            counter += 1
        else:
            counter += 1
    if guess not in chosen_word:
        lives -= 1
        print(f"you have {lives} guesses left!")
        print(hangman_dependencies.stages[lives])
    if "_" not in display:
        result = "won! Good job!"
        break

else:
    result = "lost, you suck at this lol"

print(f"The word was {chosen_word}, you {result}")
