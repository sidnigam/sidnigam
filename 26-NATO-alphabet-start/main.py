student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
phonetic_data = pandas.read_csv("./26-NATO-alphabet-start/nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for (i,row) in phonetic_data.iterrows()}
# print(phonetic_dict)    

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
word = input("Please enter a word: ").upper()
result = [phonetic_dict[phonetic] for phonetic in word if phonetic != ' ']
print(result)