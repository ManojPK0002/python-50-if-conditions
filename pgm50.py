'''Develop a program with a dynamic menu system where users can navigate through different options.
Use nested if statements to handle user input and execute the corresponding functionality.'''

while True:

    print("\nMenu:")
    print("1. Food Menu")
    print("2. Snacks Menu")
    print("3. Full Meal Menu")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # Handling user input
    if choice == "1":
        print("\nFood Menu:")
        print("1. Burger - Rs.5.00")
        print("2. Pizza - Rs.8.00")
        print("3. Salad - Rs.4.00")
        food_choice = input("Enter the number of the food item you'd like to order: ")
        if food_choice == "1":
            print("You ordered a Burger. Enjoy your meal!")
        elif food_choice == "2":
            print("You ordered a Pizza. Enjoy your meal!")
        elif food_choice == "3":
            print("You ordered a Salad. Enjoy your meal!")
        else:
            print("Invalid food choice.")
    elif choice == "2":
        print("\nSnacks Menu:")
        print("1. Chips - Rs.2.00")
        print("2. Popcorn - Rs.3.00")
        print("3. Pretzels - Rs.1.50")
        snack_choice = input("Enter the number of the snack you'd like to order: ")
        if snack_choice == "1":
            print("You ordered Chips. Enjoy your snack!")
        elif snack_choice == "2":
            print("You ordered Popcorn. Enjoy your snack!")
        elif snack_choice == "3":
            print("You ordered Pretzels. Enjoy your snack!")
        else:
            print("Invalid snack choice.")
    elif choice == "3":
        print("\nFull Meal Menu:")
        print("1. Steak Dinner - Rs.15.00")
        print("2. Fish and Chips - Rs.12.00")
        print("3. Pasta Alfredo - Rs.10.00")
        meal_choice = input("Enter the number of the meal you'd like to order: ")
        if meal_choice == "1":
            print("You ordered a Steak Dinner. Enjoy your meal!")
        elif meal_choice == "2":
            print("You ordered Fish and Chips. Enjoy your meal!")
        elif meal_choice == "3":
            print("You ordered Pasta Alfredo. Enjoy your meal!")
        else:
            print("Invalid meal choice.")
    elif choice == "4":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
