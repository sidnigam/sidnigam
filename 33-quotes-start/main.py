from tkinter import *
import requests

def get_quote():
    global canvas, quote_text
    quote = requests.get(url="https://api.kanye.rest")
    quote.raise_for_status()
    canvas.itemconfig(quote_text,text=quote.json()["quote"])


window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50)

canvas = Canvas(width=300, height=414)
background_img = PhotoImage(file="33-quotes-start/background.png")
canvas.create_image(150, 207, image=background_img)
quote_text = canvas.create_text(150, 207, text="Press the Kanye button!", width=250, font=("Arial", 30, "bold"), fill="black")
canvas.grid(row=0, column=0)

kanye_img = PhotoImage(file="33-quotes-start/kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote)
kanye_button.grid(row=1, column=0)

window.mainloop()