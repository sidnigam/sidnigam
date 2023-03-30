import json

# json.dump()   # write
# json.load()   # read
# json.update() # update

website = "test2"
email = "jane@doe.com"
password = "password-is-also-a-bad-password"

new_data = {
    website: {
        "email": email,
        "password": password,
        }
}

with open("sample.json", mode = "r") as file: # r to read
    data = json.load(file)
    print(data)
    data.update(new_data)     # JSON update method
    print(data)

with open("sample.json", mode = "w") as file: # w to write
    json.dump(data, file, indent=4)
