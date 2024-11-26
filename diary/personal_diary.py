def main():
    # Enter date and time
    date_time = input("Enter the current date and time").strip()
    
    # diary entry
    diary_entry = input("Write your diary entry: ").strip()
    
    with open("diary.txt", "a") as diary_file:
        diary_file.write(f"Date and Time: {date_time}\n")
        diary_file.write(f"Diary Entry: {diary_entry}\n")
        diary_file.write("\n")
    
    print("Your diary entry has been saved!")

if __name__ == "__main__":
    main()
