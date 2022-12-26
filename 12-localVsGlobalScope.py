################### Scope ####################

# global scope (accessible throughout the code) 
enemies = 1
ENEMIES = 23


# local scope (only accessible inside the function)
def increase_enemies():
  enemies = 2
  print(f"enemies inside function1: {enemies}")

def increase_enemies2():
  global enemies        # bad practice, don't change global variables within a function
  enemies += 2
  print(f"enemies inside function2: {enemies}")

def increase_enemies3():
  print(f"enemies inside function2: {enemies}")
  return enemies + 4    # better practice to change the global variable from inside like this

increase_enemies()
increase_enemies2()
increase_enemies3()
print(f"enemies outside function: {enemies}")