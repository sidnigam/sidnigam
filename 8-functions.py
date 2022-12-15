###!SECTION Prime number checker

n = int(input("Check this number: "))

def prime_checker(number):
    counter = 0
    for i in range(2,n):
        if n % i == 0:
            counter += 1
    if not counter == 0:
        print ("It's not a prime number.")
    else:         
        print ("It's a prime number.")
          
prime_checker(n) 

###!SECTION Paint Area Calculator

# #Write your code below this line 👇

# def round_up(number): 
#     return int(number) + (number % 1 > 0)

# def paint_calc(height, width, cover):
#     number_of_cans = round_up(height * width / cover)
#     print(f"You'll need {number_of_cans} cans of paint.")

# #Write your code above this line 👆
# # Define a function called paint_calc() so that the code below works.   

# # 🚨 Don't change the code below 👇
# test_h = int(input("Height of wall: "))
# test_w = int(input("Width of wall: "))
# coverage = 5
# paint_calc(height=test_h, width=test_w, cover=coverage)






##########!SECTION BASICS of FUNCTIONS BELOW

# # Review: 
# # Create a function called greet(). 
# # Write 3 print statements inside the function.
# # Call the greet() function and run your code.
# #!SECTION function
# def greet():
#     print('Hello')  
#     print("hi")
#     print("hola")

# greet()

# #!SECTION function with 1 input
# def greetName(name):    # name = parameter
#     print(f'Hello {name}')  
#     print(f"hi {name}")
#     print(f"hola {name}")

# greetName("Sid")        # sid = argument

# #!SECTION function with multiple inputs and positional arguments
# def greetName(name, city, state):    # name = parameter
#     print(f'Hello {name}')  
#     print(f"Looks like you live in {city}")
#     print(f"That's in the state of {state}")

# greetName("Sid","Boston", "MA")        # sid = argument

# #!SECTION function with multiple inputs and keyword arguments
# def greetName(name = "sid", city = "boston", state = "MA"):    # name = parameter
#     print(f'Hello {name}')  
#     print(f"Looks like you live in {city}")
#     print(f"That's in the state of {state}")

# greetName()        # sid = argument
