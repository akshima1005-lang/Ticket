print("===================================")
print("       TICKET BOOKING SYSTEM")
print("===================================")
print("\nAvailable Destinations:")
print("1. Delhi")
print("2. Mumbai")
print("3. Jaipur")
print("4. Bhopal")
choice = int(input("\nEnter your destination choice (1-4): "))
if choice == 1:
    destination = "Delhi"
    price = 500
elif choice == 2:
    destination = "Mumbai"
    price = 700
elif choice == 3:
    destination = "Jaipur"
    price = 600
elif choice == 4:
    destination = "Bhopal"
    price = 300
else:
    print("Invalid destination choice!")
    exit()
name = input("\nEnter passenger name: ")
age = int(input("Enter passenger age: "))
tickets = int(input("Enter number of tickets: "))
total = price * tickets
print("\n===================================")
print("          BOOKING DETAILS")
print("===================================")
print("Passenger Name :", name)
print("Passenger Age  :", age)
print("Destination    :", destination)
print("Ticket Price   : ₹", price)
print("Number of Tickets:", tickets)
print("Total Amount   : ₹", total)
print("===================================")
print("      TICKET BOOKED SUCCESSFULLY!")
print("===================================")
