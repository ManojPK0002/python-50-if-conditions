'''Flight Booking System:

Develop a program for a flight booking system. Consider factors such as seat availability,
 passenger age, and class preference. Use nested if statements to determine if a booking is successful
 and calculate the ticket price.
 classes=economy, premium economy, business, and first class
'''


seats = {"economy": 50,"premium_economy": 30,"business": 20,"first_class": 10}

passenger_age = int(input("Enter passenger age: "))
passenger_class = input("Enter class preference ").lower()

if passenger_age<=2:
    print("Ticket is free for your baby")
if passenger_age>18:
    discount=0.05#(5%)
else:
    discount=0.2#(20%)

if (passenger_age<=2):
    exit()
if (passenger_class in seats ):
    price={"economy":300,"premium_economy":500,"business":750 ,"first_class":1000}
    ticket_price=price[passenger_class]-price[passenger_class]*discount
    print(f"Ticket price: {ticket_price}")
    print("Booking successful")
    seats[passenger_class]=seats[passenger_class]- 1
else:
    print("The class is full or entered invalid class")
