# days of the week
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# steps
steps = []

# ask how many steps they took 
for day in days:
    step_count = int(input(f"How many steps did you take on {day}? "))
    steps.append(step_count)  

# steps per day
i = 0
while i < 7:  
    print(f"{days[i]}: {steps[i]} steps")
    i += 1

# total steps
total_steps = 0
i = 0
while i < 7:
    total_steps += steps[i]
    i += 1
print(f"\nTotal steps taken in the week: {total_steps}")

# average steps
average = round(total_steps / 7) 
print(f"Average steps per day: {average}")
