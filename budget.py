#total budget
Budget = float(input("What is your total budget?"))

#spending categories
Rent = float(input("How much do you pay for Rent?"))
Utilities = float(input("How much do you pay for Utilities?"))
Grcoeries = float(input("How much do you pay for Groceries?"))
Transportation = float(input("How much do you pay for Transportation?"))
Health_Care = float(input("How much do you pay for Health Care?"))
Personal_Care = float(input("How much do you pay for Personal Care?"))
Clothing = float(input("How much do you pay for Clothing?"))
Debt = float(input("How much do you pay for Debt?"))

#conversion into percentage
R_p = (Rent / Budget) * 100
U_p = (Utilities/ Budget) * 100
G_p = (Grcoeries/Budget)* 100
T_p= (Transportation/Budget)* 100
H_p= (Health_Care/Budget)* 100
P_p = (Personal_Care/Budget)* 100
C_p = (Clothing/Budget)* 100
D_p = (Debt/Budget)* 100

#results
print(f"{"Rent"}: {R_p:.2f}%")
print(f"{"Utilities"}: {U_p:.2f}%")
print(f"{"Groceries"}: {G_p:.2f}%")
print(f"{"Transportation"}: {T_p:.2f}%")
print(f"{"Health Care"}: {H_p:.2f}%")
print(f"{"Personal Care"}: {P_p:.2f}%")
print(f"{"Clothing"}: {C_p:.2f}%")
print(f"{"Debt"}: {D_p:.2f}%")
