import time
from flask import Flask
import random

app = Flask(__name__)

colors = ['red', 'green', 'blue', 'orange', 'purple', 'maroon', 'violet']

def color(function):
    def wrapper(*args, **kwargs):
        chosen_color = random.choice(colors)
        return f'<h1 style="color:{chosen_color};">{function()}</h1>'
    return wrapper

@app.route("/")
@color
def home():
    return "Guess a number between 1 to 9" \
    f"<div style='text-align: center'>" \
    f"<img width=300 src = 'https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif'>"

nums = range(1,10)
chosen_number = random.choice(nums)
print(chosen_number)

@app.route("/<int:user_num>")
# @color potential bug not being able to use it more than once
def check(user_num):
    if user_num == chosen_number:
        return "Bingo! You got it you little genius"
    if user_num > chosen_number:
        return "Too highhhhh"
    else:
        return "Too low"    

if __name__ == "__main__":
    app.run(debug=True)
