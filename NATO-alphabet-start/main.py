import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")

data_dict = {row.letter:row.code for (index, row) in df.iterrows()}

name = input("What's your name? ").upper()
name_codes = [data_dict[letter] for letter in name]
print(name_codes)
