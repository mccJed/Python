#Dictionary
nato_alphabet = {
    "A": "Alpha", "B": "Bravo", "C": "Charlie", "D": "Delta", "E": "Echo",
    "F": "Foxtrot", "G": "Golf", "H": "Hotel", "I": "India", "J": "Juliett",
    "K": "Kilo", "L": "Lima", "M": "Mike", "N": "November", "O": "Oscar",
    "P": "Papa", "Q": "Quebec", "R": "Romeo", "S": "Sierra", "T": "Tango",
    "U": "Uniform", "V": "Victor", "W": "Whiskey", "X": "X-ray", "Y": "Yankee",
    "Z": "Zulu"
}

# Function
def spell_word_nato(word):
    for letter in word.upper():
        if letter in nato_alphabet:
            print(nato_alphabet[letter])
        else:
            print(f"'{letter}' is not a valid letter in the NATO alphabet.")

def main():
    user_input = input("Enter a word: ")
    spell_word_nato(user_input)

main()
