from tkinter import *
from tkinter import messagebox
import random
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generatePassword():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = []
    password_numbers = []
    password_symbols = []

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]

    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    passwordEntry.delete(0,END)
    passwordEntry.insert(0,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def addPasswordButtonClick():
    website = websiteEntry.get()
    email = emailEntry.get()
    password = passwordEntry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Please populate all the details!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details to be entered: \nEmail: {email} \nPassword: {password}")
        if is_ok:
            with open("29-password-manager-start/sample.txt", mode = "a") as file: 
                file.write(f"\n{website} | {email} | {password} ")
            websiteEntry.delete(0,END)
            passwordEntry.delete(0,END)
            websiteEntry.focus()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
passwordImage = PhotoImage(file="./29-password-manager-start/logo.png")
canvas.create_image(100, 100, image=passwordImage)
canvas.grid(row=1, column=2)

# Buttons 
generatePassword = Button(text="Generate Password", command=generatePassword)
generatePassword.grid(row=4, column=3)

addPassword = Button(text="Add", width=36, command=addPasswordButtonClick)
addPassword.grid(row=5, column=2, columnspan=2)

# Labels
websiteLabel = Label(text="Website:")
websiteLabel.grid(row=2, column=1)

emailLabel = Label(text="Email/Username:")
emailLabel.grid(row=3, column=1)

passwordLabel = Label(text="Password:")
passwordLabel.grid(row=4, column=1)

# Entries
websiteEntry = Entry(width=38)
websiteEntry.grid(row=2,column=2,columnspan=2)
websiteEntry.focus()

emailEntry = Entry(width=38)
emailEntry.grid(row=3,column=2,columnspan=2)
# pre-populating a default email
emailEntry.insert(0,"jane@doe.com")

passwordEntry = Entry(width=21)
passwordEntry.grid(row=4,column=2)

window.mainloop()