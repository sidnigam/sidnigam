import pandas
from tkinter import *
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    spanish_data = pandas.read_csv("./31-flash-card-project/updated_spanish_progress.csv")
except FileNotFoundError:
    spanish_data = pandas.read_csv("./31-flash-card-project/spanish.csv")
learn = spanish_data[:100].to_dict(orient="records")
# sample_word = spanish_data.english[100]
# print((sample_word))
# print(learn)

# ---------------------------- BUTTON SETUP ------------------------------- #
def rightClick():
    learn.remove(current_card)
    # print(len(learn))
    buttonClick()

def buttonClick():
    global current_card, flip_timer
    canvas.itemconfig(canvas_image, image=cardfront)
    window.after_cancel(flip_timer)
    current_card = random.choice(learn)
    current_word = current_card["word"]
    canvas.itemconfig(title, text="Spanish",fill="black")
    canvas.itemconfig(word, text=current_word,fill="black")
    flip_timer = window.after(3000, func=flipCard)

def flipCard():
    english_translation = current_card["english"]
    canvas.itemconfig(canvas_image, image=cardback)
    canvas.itemconfig(title, text="English", fill="white")
    canvas.itemconfig(word, text=english_translation, fill = "white")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Language Learner")
window.config(padx=50, pady=50)
window['background']=BACKGROUND_COLOR

canvas = Canvas(width=800, height=526)
cardback  = PhotoImage(file="./31-flash-card-project/images/card_back.png")
cardfront = PhotoImage(file="./31-flash-card-project/images/card_front.png")
right     = PhotoImage(file="./31-flash-card-project/images/right.png")
wrong     = PhotoImage(file="./31-flash-card-project/images/wrong.png")

canvas_image = canvas.create_image(400, 263, image=cardfront)
canvas.grid(row=1, column=1, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR,highlightthickness=0)
title = canvas.create_text(400,150, text="Title", font=("Arial",40,"italic"),fill='black')
word = canvas.create_text(400,253, text="Text", font=("Arial",60,"bold"),fill='black')

# Buttons 
wrongButton = Button(image=wrong, highlightthickness=0, highlightbackground=BACKGROUND_COLOR)
wrongButton.grid(row=2, column=1)
wrongButton.config(command=buttonClick)

rightButton = Button(image=right, highlightthickness=0, highlightbackground=BACKGROUND_COLOR)
rightButton.grid(row=2, column=2)
rightButton.config(command=rightClick)

flip_timer = window.after(3000, func=flipCard)

buttonClick()

window.mainloop()

learn_csv = pandas.DataFrame(learn)
learn_csv.to_csv("./31-flash-card-project/updated_spanish_progress.csv",index=False)