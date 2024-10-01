#factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

#main function
def main():
    number = int(input("Enter a non-negative integer: "))
    
    # Ensure that the input is non-negative
    if number < 0:
        print("Please enter a non-negative integer.")
    else:
        result = factorial(number)
        print(f"The factorial of {number} is {result}.")
main()
