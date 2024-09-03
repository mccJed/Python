# sample weights in kilograms
s_1 = 12
s_2 = 86
s_3 = 5
s_4 = 2.2

# Conversion factor: 1 kilogram = 2.20462 pounds
conversion_factor = 2.20462

# Calculations
kilogram_1 = s_1 * conversion_factor
kilogram_2 = s_2 * conversion_factor
kilogram_3 = s_3 * conversion_factor
kilogram_4 = s_4 * conversion_factor

# Output
print(f"{s_1} kilograms is equal to {kilogram_1:.2f} pounds.")
print(f"{s_2} kilograms is equal to {kilogram_2:.2f} pounds.")
print(f"{s_3} kilograms is equal to {kilogram_3:.2f} pounds.")
print(f"{s_4} kilograms is equal to {kilogram_4:.2f} pounds.")