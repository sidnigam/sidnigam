
##!SECTION Types of errors
# # key error
# a_dictionary = {"key": "value"}
# value = a_dictionary["non_existent_key"]

# # index error
# fruits = ["apple","pear","banana"]
# fruit = fruits[4]

# # type error
# text = 'abc'
# print(text + 5)

##!SECTION Error handling methods
# try: # something that might cause an exception
# except: # do this if there WAS an exception
# else: # do this if there were NO exceptions
# finally: # do this no matter what happens

##!SECTION Example
try:
    file = open("a_file.txt")
    a_dictionary = {"key":"value"}
    # print(a_dictionary["test-wrong-key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("file was closed")
    raise TypeError("This is a made up error") # can use this for raising errors when the code technically works but it shouldn't (like human heights for example)

