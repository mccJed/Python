import calendar
from datetime import datetime

def main():
    current_year = datetime.now().year

    while True:
        try:
            # input birth month
            birth_month = input("Enter your birth month (1-12): ")


            # Convert birth_month to an integer
            birth_month = int(birth_month)

            # Generate the calendar for the birth month and current year
            cal = calendar.TextCalendar()
            month_calendar = cal.formatmonth(current_year, birth_month)

            # Display the calendar
            print("\nHere is the calendar for you birth month in the current year.:")
            print(month_calendar)
            break 

        except ValueError as e:
            print(f"Error: {e}. Enter valid integer (1-12)")

if __name__ == "__main__":
    main()
