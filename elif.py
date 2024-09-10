#Numeric grade
grade= float(input("What did you get on the test?"))

#numeric into letter
if grade < 60:
    print("The letter grade is F")
elif grade >= 60 and grade < 70:
    print("the letter grade is D")
elif grade >=70 and grade <80:
    print("the letter grade is C")
elif grade >= 80 and grade < 90:
    print("the letter grade is B")
elif grade >90:
    print("the letter grade is A")