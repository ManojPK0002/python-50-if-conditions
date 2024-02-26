"""fruits=['apple','banana','orange','mango','kiwi']
for i in fruits:
    if 'a' in i:
        fruits.remove(i)
print(fruits)

"""
balance = 0
while True:
    print("""
    Welcome to the ATM system!
    1. Check balance
    2. Withdraw money
    3. Deposit funds
    4. Exit
    """)
    choice = input("Enter your choice: ")

    if choice == '1':
        print("Your current balance is:", balance)

    elif choice == '2':
        amount = float(input("Enter the amount you want to withdraw: "))
        if amount > balance:
            print("Insufficient funds!")
        else:
            balance -= amount
            print("You have withdrawn:", amount)
            print("Your updated balance is:", balance)

    elif choice == '3':
        amount = float(input("Enter the amount you want to deposit: "))
        balance += amount
        print("You have deposited:", amount)
        print("Your updated balance is:", balance)

    elif choice == '4':
        print("Exiting the ATM system...")
        break

    else:
        print("Invalid choice! Please try again.")