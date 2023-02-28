from tkinter import *

window = Tk()

window.title("Miles to KM converter")
# window.minsize(width = 500, height = 300)

l1 = Label(padx=10, pady=10, text="miles")
l1.grid(row=1, column=3)

l2 = Label(padx=10, pady=10, text="is equal to")
l2.grid(row=2, column=1)

l3 = Label(padx=10, pady=10, text="0")
l3.grid(row=2, column=2)

l4 = Label(padx=10, pady=10, text="KM")
l4.grid(row=2, column=3)

def button_clicked():
    l3.config(text=round(int(input.get())*1.6,2))

button = Button(text="Calculate", command=button_clicked)
button.grid(row=3, column=2)

# Entry

input = Entry(width = 20)
input.grid(row=1, column=2)

window.mainloop()


