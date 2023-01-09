class User:                                 # Blueprint - class
    def __init__(self, user_id, username):
        print("you are now being created")  # init function (special function called
                                            # everytime an object is created from this class)
        self.id = user_id
        self.username = username            # creates a required parameter
        self.followers = 0                  # all attributes will start with this value
        self.following = 0                  # these are all attributes

    def follow(self, user):                 # this is a method (function associated with object/class)
        user.followers += 1
        self.following += 1

#!SECTION Creating objects and attributes from initializer 

user_2 = User("2022","sidnigam")        # init is called everytime this is created
                                        # 2 attributes are created by default based on the class definition
print(user_2.username) 

user_1 = User("002","siddd")                

user_1.id = "001"                       # attribute can be changed
user_1.username = "sid"         

print(user_1.username)

#!SECTION Creating objects and attributes from initializer

user_1.follow(user=user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)