import time 

# def outer():
#     print("yoyoyo im outside")
#     def inner():
#         print("yoyo im inside")
#     return inner

# checker = outer()
# checker()

def delay_decorator(function):
    def wrapper():
        time.sleep(2)
        function()
        function()
    return wrapper

@delay_decorator
def say_hello():
    print("hello")

def say_sup():
    print("sup")

@delay_decorator
def say_bye():
    print("bye")

# say_hello()
# say_sup()
# say_bye()

new_fun = delay_decorator(say_sup)
# new_fun()

# print(time.time())

def speed_calculator_decorator(function):
    def timewrapper():
        initial_time = float(time.time())
        function()
        final_time = float(time.time())
        print(f"{function.__name__} run speed: {final_time - initial_time}s")
        # time_for_function = float(final_time) - float(initial_time)
    return timewrapper

@speed_calculator_decorator
def fast_function():
    for i in range(100000):
        i * i    

@speed_calculator_decorator
def slow_function():
    for i in range(100000):
        i ^ i - i

fast_function()
slow_function()