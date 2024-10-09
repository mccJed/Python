import random

def main():
    random_number = random.randint(1, 100)
    
    print("I am thinking of a number between 1 and 100")
    
    while True:
        try:
            #Guessing the number
            guess = int(input("Enter your guess: "))
            
            if guess == random_number:
                print("You did it!")
                break
            
            # Calculate absolute difference
            difference = abs(random_number - guess)
            
            # Feedback depending how how close the guess was
            if difference <= 5:
                print("Very Hot!")
            elif difference <= 15:
                print("Hot!")
            elif difference <= 25:
                print("Cool!")
            else:
                print("Cold!")
        
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    
if __name__ == "__main__":
    main()
