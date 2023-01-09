import random
import upperlower_dependencies

group = list(range(len(upperlower_dependencies.data)))
points = 0

# def game():

A = random.choice(group)
group.remove(A)

B = random.choice(group)
# group.remove(B)


game_over = False

while not game_over:

    A_data = upperlower_dependencies.data[A]
    B_data = upperlower_dependencies.data[B]

    print( f'''
    {upperlower_dependencies.logo}
    Compare A: {A_data['name']}, a {A_data['description']}, from {A_data['country']}
    {upperlower_dependencies.vs}
    Compare B: {B_data['name']}, a {B_data['description']}, from {B_data['country']}
    ''')
    guess = input("Who has more followers? Type 'A' or 'B': ")

    if guess == "A":
        if A_data['follower_count'] > B_data['follower_count']:
            points += 1
            print(f"You're right! Current score: {points}")           
            A = B
            B = random.choice(group)
            group.remove(B)
        else:
            print(f"Sorry, that's wrong. Final score: {points}")
            game_over = True

    elif guess == "B":
        if B_data['follower_count'] > A_data['follower_count']:
            points += 1
            print(f"You're right! Current score: {points}")           
            A = B
            B = random.choice(group)
            group.remove(B)
        else:
            print(f"Sorry, that's wrong. Final score: {points}")
            game_over = True
    else:
        print("Invalid guess. Please type 'A' or 'B' as your response.")

# game()

        # 'name': 'Emma Watson',
        # 'follower_count': 56,
        # 'description': 'Actress',
        # 'country': 'United Kingdom'

