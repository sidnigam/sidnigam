import pandas

data = pandas.read_csv("2018-NYC_Squirrel_Data.csv")
color = data["Primary Fur Color"]
print(color.value_counts())