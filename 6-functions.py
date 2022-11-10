def my_function():
    print("hello")
    print("bye")
    print(len("bye"))
    
my_function()

x = 10

while x > 4:
    print(f"x is {x}")
    x -= 1

goal = 10 

while goal() != True:        # same as below
    print("Not at goal")

while not goal():            # same as above    
    print("Not at goal")

while not at_goal():
    if front_is_clear() == True:
        move()
    elif wall_in_front() == True:
        jump()