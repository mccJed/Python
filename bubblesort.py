# Ask for 5 names
names = []
for i in range(5):
    name = input(f"Enter name {i+1}: ")
    names.append(name)

swapped = True
while swapped:
    swapped = False 
    for i in range(len(names) - 1):
    
        if names[i] > names[i + 1]:
            swapped = True  
            names[i], names[i + 1] = names[i + 1], names[i]

# Aphabetical order
print("\nNames in alphabetical order:")
for name in names:
    print(name)

# Reverse
names.reverse()
print("\nReverse alphabetical:")
for name in names:
    print(name)
