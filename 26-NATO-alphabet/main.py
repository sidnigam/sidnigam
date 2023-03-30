import pandas
#TODO 1. Create a dictionary in this format:
phonetic_data = pandas.read_csv("./26-NATO-alphabet/nato_phonetic_alphabet.csv")
phonetic_dict = {row.letter:row.code for (i,row) in phonetic_data.iterrows()}
# print(phonetic_dict)    

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def converter(word):
    try: 
        result = [phonetic_dict[phonetic] for phonetic in word if phonetic != ' ']
    except KeyError as message:
        print(f"Please enter only letters, spaces are fine")
        word = input("Please enter a word: ").upper()
        converter(word)
    else: print(result)

spell = input("Please enter a word: ").upper()
converter(spell)