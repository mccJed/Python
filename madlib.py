def custom_song(animal, verb, noun,evil, animal_2, adjective,adjective_2, noun_2 ):
    print(f"{animal}man {animal}man")
    print(f"Does what ever a {animal} can")
    print(f"{verb}s a {noun} any size")
    print(f"Catches {evil} just like {animal_2}")
    print(f"Look out! \n Here comes {animal}man")
    print(f"Is he {adjective}?")
    print(f"Listen bud")
    print(f"He's got {adjective_2} blood")
    print(f"Can he swing from a {noun_2}?")
    print(f"Take a look overhead!")
    print(f"Look out! \n Here comes {animal}man")

input_animal = input("Enter an animal: ")
input_verb= input("Enter a verb: ")
input_noun=input("Enter a noun: ")
input_evil= input("Enter a group of evil people ie: thieves: ")
input_animal_2=input("Enter an animal (plural): ")
input_adjective= input("Enter an Adjective: ")
input_adjective_2= input("Enter an Adjective: ")
input_noun_2=input("Enter a noun: ")



custom_song(animal=input_animal,
    verb=input_verb,
    noun=input_noun,
    evil=input_evil,
    animal_2=input_animal_2,
    adjective=input_adjective,
    adjective_2=input_adjective_2,
    noun_2=input_noun_2
    )