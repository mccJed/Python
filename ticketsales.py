# Step 1: Initialize the seating list (seats 1 to 20)
available_seats = list(range(1, 21))

#Display Available Seats
print("These are the Available seats \n", available_seats)
ticket = int(input("Enter the seat you would like to purchase, Type 0 to end transaction"))
while ticket != 0:
    if ticket in available_seats:
         available_seats.remove(ticket)
    else:
       print("Please enter a valid seat")
    print (available_seats)
    ticket = int(input("Enter the seat you would like to purchase, Type 0 to end transaction"))
    
if ticket == 0:
    print("thank you for your purchase")


   

