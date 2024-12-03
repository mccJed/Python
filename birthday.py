# calculate a person's age in: Years, months, weeks, days
# 30.41 days in a month
# 7 days in a week 

from datetime import datetime

def main():

    try:
     
        today = datetime.today()
        birth_year = int(input("What year were you born? "))
        month = int(input("What month were you born (as a number, e.g., May = 5)? "))
        day = int(input("What day of the month were you born? "))
        birthday = datetime(birth_year, month, day)

        birthday_output = birthday.strftime("%Y-%m-%d")
        print(f"Your birthday is: {birthday_output}")

        # Calculate the time difference
        delta = today - birthday

        # Days difference
        total_days = delta.days
        print(f"Difference is {total_days} days")

        # Approximate years calculation 
        delta_years = total_days // 365.2425
        print(f"You are {int(delta_years)} years old")

        # Approximate months calculation
        delta_months = int(total_days // 30.41)  
        print(f"You are approximately {delta_months} months old")

        # Weeks calculation
        delta_weeks = total_days // 7  
        print(f"You are approximately {delta_weeks} weeks old")

        # Total hours and minutes
        total_seconds = delta.total_seconds()
        total_hours = total_seconds // 3600  # 3600 seconds in an hour
        total_minutes = total_seconds // 60  # 60 seconds in a minute

        # Print hours and minutes
        print(f"You are approximately {int(total_hours)} hours old")
        print(f"You are approximately {int(total_minutes)} minutes old")

    except Exception as e:
        print(f"ooooops!!!:  {e}") 
        main()
main()