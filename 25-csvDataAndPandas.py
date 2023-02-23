# read mode
with open("weather_data.csv", mode = "r") as file:
    data = file.readlines()
        
# print(data)

import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        try:
            temperatures.append(int(row[1]))
        except ValueError:
            continue
print(temperatures)

import pandas

data = pandas.read_csv("weather_data.csv")
print(data)
# print(type(data['temp']))
# print(type(data))

data_dict = data.to_dict()
print(data_dict)

temp_list = data["temp"].to_list()
print(temp_list)

avg_temp = data["temp"].max()
print(avg_temp)

print(data.temp.mean())

row = data[data.temp == data.temp.max()]
print(row)

monday = data[data.day == "Monday"]
print(monday.temp/5 * 9 + 32)

# create a dataframe from scratch

data_dict = {
    "students": ["Amy", "Santiago", "James"],
    "scores": [76, 65, 66]
}

data2 = pandas.DataFrame(data_dict)
print(data2)
print(data2[data2.scores == data2.scores.max()])
data2.to_csv("new_data.csv")