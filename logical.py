#ask for two numbers
number_1= int (input("Enter a random number"))
number_2 =int (input("Enter a different random number"))

#logical comparison 1
if number_1 %2== 0 and number_2 %2 ==0:
    print("Both numbers are even")
elif number_1 %2 == 0 and number_2 %2 !=0:
    print("one number is even")
elif number_2 %2 ==0 and number_1 %2 !=0:
    print("one number is even and one is odd")
else :
    print("both numbers are odd")
    
#2
if number_1 > number_2:
    print(number_1,">" , number_2)
else: print(number_2, ">", number_1)

#3
sum = number_1 + number_2
print ("the sum of the two numbers is", sum)

#4
if number_1 > 100 and number_2 > 100:
    print(number_1, "and", number_2,">100")
elif number_1 >100 and number_2 <100:
    print(number_1,">100\n", number_2, "<100")
elif number_2 >100 and number_1 <100:
    print(number_2,">100\n", number_1, "<100")
else :
    print(number_1, "and", number_2,"<100")
#5
difference = number_1 - number_2
print ("the first number minus the second number is", difference)
#6
product = number_1 * number_2
print ("the product of the two numbers is", product)