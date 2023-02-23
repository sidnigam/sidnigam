with open("./26-data-overlap/file1.txt", mode = "r") as file:
    contents1 = file.readlines()
    contents1 = [int(num) for num in contents1]
    print(contents1)

with open("./26-data-overlap/file2.txt", mode = "r") as file:
    contents2 = file.readlines()
    contents2 = [int(num) for num in contents2]
    print(contents2)

intersect = [num for num in contents1 if num in contents2]
print(intersect)
# import pandas as p

# data1 = p.read_csv("./26-data-overlap/file1.txt")

# print(data1)


#Write your code 👆 above:

# print(result)