# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

remainingAge = 90 - int(age)
daysLeft = remainingAge * 365
weeksLeft = remainingAge * 52 
monthsLeft = remainingAge * 12

print(f"You have {daysLeft} days, {weeksLeft} weeks, and {monthsLeft} months left.")


#Data Types

#String
print("Hello World")

#Integer
print(123+345)
print(100_000+800_350)

#Float
print(3.1415)
num = "12"
new_num = float(num)

#Boolean
# (True, False)

print(type(True))