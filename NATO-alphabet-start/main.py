import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")

data_dict = {row.letter: row.code for (index, row) in df.iterrows()}

is_running = True

while is_running:
    name = input("Enter a word: ").upper()

    try:
        name_codes = [data_dict[letter] for letter in name]
    except KeyError:
        print("Sorry. Only letters in the alphabets please.")
    else:
        print(name_codes)
        is_running = False
