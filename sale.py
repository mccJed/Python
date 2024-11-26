def main():
    try:
        with open("sales_totals.txt", "r") as file:
            total = 0.0
            count = 0
            
            print("Sales Totals:")
            
            for line in file:
                amount = float(line.strip())
                total += amount
                count += 1
        
                print(f"{amount:,.2f}")
            
            #average
            average = total / count if count > 0 else 0
            
            # Display total, count, and average
            print("\nSummary:")
            print(f"Total: {total:,.2f}")
            print(f"Number of entries: {count}")
            print(f"Average: {average:,.2f}")
    
    except FileNotFoundError:
        print("Error: The file 'sales_totals.txt' was not found.")
    except ValueError:
        print("Error: The file contains invalid data that cannot be converted to a float.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
