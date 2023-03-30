import pandas

BACKGROUND_COLOR = "#B1DDC6"

spanish_data = pandas.read_csv("./31-flash-card-project/spanish.csv")
print(spanish_data.word[100])

sample_word = spanish_data.english[100]
print((sample_word))
