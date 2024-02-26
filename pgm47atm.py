
balance=int(input("Enter how much you would like to have in your account"))
print("1. Check balance \t 2. Withdraw money \t 3. Deposit  \t 4. Exit")
choice = input("Enter your choice: ")
if choice == '1':
    print("current balance is:", balance)
elif choice == '2':
    amount = int(input("Enter the amount you want to withdraw: "))
    if amount > balance:
        print("Insufficient funds")
    else:
        balance = balance-amount
        print("withdrawn amount is:", amount)
        print("balance is:", balance)
elif choice == '3':
    amount = int(input("Enter the amount you want to deposit: "))
    balance=balance+ amount
    print(" deposited amount is:", amount)
    print("balance is :", balance)
elif choice == '4':
    print("Exiting the ATM system...")
    exit()
else:
    print("Invalid choice! Please try again.")
