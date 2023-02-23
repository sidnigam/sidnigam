import turtle as t
import pandas

screen = t.Screen()
screen.title("US States Game")
image = "/Users/sidnigam/Documents/coding/sidnigam/25-us-states-game-start/states.gif"
screen.addshape(image)

t.shape(image)
answer_state = screen.textinput("Guess the state", "What's a state's name?")
answer = answer_state.title()
score = 0
data = pandas.read_csv("/Users/sidnigam/Documents/coding/sidnigam/25-us-states-game-start/50_states.csv")
correct_guesses = []

while score < 50:
    if answer == "Exit":
        break
    if answer in data.state.values:
        state_turtle = t.Turtle()
        state_turtle.speed(0)
        state_turtle.hideturtle()
        state_turtle.penup()
        if answer not in correct_guesses:
            score += 1
            state_turtle.goto(x = int(data.x[data.state == answer]), y = int(data.y[data.state == answer]))
            correct_guesses.append(answer)
            state_turtle.write(answer)
            answer_state = screen.textinput(f"Guessed: {score}/50", "What's another state's name?")
            answer = answer_state.title()
        else:
            answer_state = screen.textinput(f"Already guessed, try another! Score: {score}/50", "What's another state's name?")
            answer = answer_state.title()
    else:
        answer_state = screen.textinput(f"Guessed: {score}/50", "Wrong! Guess another state's name?")
        answer = answer_state.title()

print(correct_guesses)   

