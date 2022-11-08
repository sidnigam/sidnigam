#Write your code below this line 👇

bill = float(input("What was the total bill? "))
people = float(input("How many people are there? "))
percent = float(input("How much would you like to tip? 10%, 12% or 15%? "))

tip = round(bill * (1 + percent / 100) / people, 2)
tip = "{:.2f}".format(tip)
print(f"Each person should pay: ${tip}")