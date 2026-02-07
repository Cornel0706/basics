import pandas
data = pandas.read_csv("nato_phonetic_alphabet.csv")

# Create a dictionary in this format:
nato_dict = {row.letter:row.code for (index, row) in data.iterrows()}
# Create a list of the phonetic code words from a word that the user inputs.
def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        result = [nato_dict[letter] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet")
        generate_phonetic()
    else:
        print(result)

generate_phonetic()

