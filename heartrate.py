# time slot and heart rate
time_slots = ["Morning", "Midday", "Afternoon", "Evening"]
heart_rates = []

#ask for heart rates
for time in time_slots:
    heart_rate = int(input(f"Enter your heart rate (in BPM) at {time}: "))
    heart_rates.append([time,heart_rate])
#average
total = 0
for heart_rate in heart_rates:
    total = total + heart_rate[1] 
average = round(total/len(heart_rates))

print(f"\nAverage heart rate: {average:.2f} bpm")

