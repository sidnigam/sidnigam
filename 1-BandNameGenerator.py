#1. Create a greeting for your program.
greeting = """
Hello there!
Welcome to my first project
  ___________________________
~~| THE BAND NAME GENERATOR |~~
  ---------------------------
For this project, I will ask you a few questions, sound good?

"""

print(greeting)

#2. Ask the user for the city that they grew up in.

city = input("1. What city did you grow up in?\n")

#3. Ask the user for the name of a pet.

pet = input("\n2. What is the name of your pet?\n")

#4. Combine the name of their city and pet and show them their band name.

print("Generating random band name")
import time

time.sleep(2)
print("... still thinking")
time.sleep(2)
print("Your band name is The " + city + " " + pet + "s")
#5. Make sure the input cursor shows on a new line, see the example at:
#   https://replit.com/@appbrewery/band-name-generator-end
