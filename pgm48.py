'''Game Character Interaction:
Design a text-based game where the player controls a character.
Use nested if statements to handle different interactions based on the player's choices, leading to multiple possible outcomes.
'''
#i am new addition 
print("Welcome to the Forest Adventure!")
print("\nYou find yourself in a dense forest. You can go 'left', 'right', or 'straight'.")
choice1 = input("Which way do you want to go? ")

if choice1 == "left":
    print("\nYou encounter a bear! What do you do?")
    action = input("Do you 'run' or 'hide'? ")

    if action == "run":
        print("\nYou manage to not caught from the bear and find a hidden cave.")
        print("Inside the cave, you find a treasure chest.")
        print("Congratulations, you win!")
    elif action == "hide":
        print("\nThe bear finds you and you lose the game. Game over.")
    else:
        print("\nInvalid choice. Game over.")

elif choice1 == "right":
    print("\nYou come across a river. Do you 'swim' across or 'follow' the river?")
    action = input("What is your choice? ")

    if action == "swim":
        print("\nYou swim across the river and find a path leading to a village.")
        print("You reach the village safely. Congratulations, you win!")
    elif action == "follow":
        print("\nYou follow the river and get lost in the forest. Game over.")
    else:
        print("\nInvalid choice. Game over.")

elif choice1 == "straight":
    print("\nYou walk straight ahead and encounter a pack of wolves.")
    print("What do you do?")
    action = input("Do you 'fight' or 'run'? ")

    if action == "fight":
        print("\nYou fight with the wolves and continue your journey.")
        print("After a while, you reach a road and find your way back home. Congratulations, you win!")
    elif action == "run":
        print("\nYou try to run but the wolves catch up to you. Game over.")
    else:
        print("\nInvalid choice. Game over.")

else:
    print("\nInvalid choice. Game over.")
