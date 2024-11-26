def two_letter_combinations(characters):

    for char1 in characters:
        for char2 in characters:
            yield char1 + char2

def main():
 
    #list of 5 characters
    character_list = ['j', 'e', 'd', 'q', 'r']

    combinations = two_letter_combinations(character_list)
    
    # Print each combination
    print("Two-letter combinations:")
    for combo in combinations:
        print(combo)

main()
