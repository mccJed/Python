#conversion metric
POUNDS_TO_KG = 0.453592  
INCHES_TO_M = 0.0254    

#conversion
def calculate_bmi(weight_in_pounds, height_in_inches):
    weight_in_kg = weight_in_pounds * POUNDS_TO_KG  
    height_in_m = height_in_inches * INCHES_TO_M   
    bmi = weight_in_kg / (height_in_m ** 2)         
    return bmi

#user input
while True:
    try:
        weight = float(input("Please enter your weight in pounds: "))
        if weight > 0:
            break
        else:
            print("Please enter a positive value for weight.")
    except ValueError:
        print("Invalid input. Please enter a valid number for weight.")

while True:
    try:
        height = float(input("Please enter your height in inches: "))
        if height > 0:
            break
        else:
            print("Please enter a positive value for height.")
    except ValueError:
        print("Invalid input. Please enter a valid number for height.")

def determine_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"
    
bmi = calculate_bmi(weight, height)

category = determine_bmi_category(bmi)

print(f"Your BMI is: {bmi:.2f}")
print(f"You are in the {category} category")