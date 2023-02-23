
# append mode
with open("20-snake/sample.txt", mode = "a") as file: 
    file.write("\nNew text.")

# read mode
with open("../sidnigam/20-snake/sample.txt", mode = "r") as file:
    contents = file.read()
    print(contents)

# write mode (replaces current text in the file)
with open("../sidnigam/20-snake/sample.txt", mode = "w") as file:
    file.write("\nWrite mode.")

    