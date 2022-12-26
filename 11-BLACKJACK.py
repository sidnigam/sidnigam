logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random



# Create initialization variables
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer_cards = []
dealer_score = 0
user_cards = []
user_score = 0

def initialize():
    dealer_cards.clear()
    dealer_score == 0
    user_cards.clear()
    user_score == 0

lose_message_dealer = "You lose 😤"
lose_message_over = "You went over. You lose 😭"
win_message = "You win 😃"
win_message_over = "Dealer went over. You win 😃"
draw_message = "It's a draw!"

def deal():
    return random.choice(cards)

def replace_values(list_to_replace, item_to_replace, item_to_replace_with):
    return [item_to_replace_with if item == item_to_replace else item for item in list_to_replace]

def calculate_sum(list):
    if list.count(11) and sum(list) > 21:
        list = replace_values(list, 11, 1)
        return sum(list)
    return(sum(list))

def result():
    dealer_score = calculate_sum(dealer_cards)
    user_score = calculate_sum(user_cards)
    while dealer_score < 17:
        dealer_cards.append(random.choice(cards))
        dealer_score = calculate_sum(dealer_cards)
    print(f"Dealer's cards: {dealer_cards}, dealer's score: {dealer_score}")
    if user_score > 21:
        return lose_message_over
    elif dealer_score > 21 and user_score < 22:
        return win_message_over
    elif dealer_score < user_score:
        return win_message
    elif dealer_score == user_score:
        return draw_message
    elif dealer_score > user_score:
        return lose_message_dealer

def play():
    initialize()
    dealer_cards.append(random.choice(cards))
    dealer_score = calculate_sum(dealer_cards)

    user_cards.append(random.choice(cards))
    user_cards.append(random.choice(cards))
    user_score = calculate_sum(user_cards)

    print(f"{logo}\n\n")
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Dealer's first card: {dealer_cards}")
    decision = input("Type 'y' to get another card, type 'n' to pass: ")

    while decision == "y":
        user_cards.append(random.choice(cards))
        user_score = calculate_sum(user_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        decision = input("Type 'y' to get another card, type 'n' to pass: ")
    print(result())
    again = input("Would you like to play again?\nType 'y' for yes and 'n' for no \n")
    if again == 'y':
        initialize()
        play()
    else:
        exit()

play()