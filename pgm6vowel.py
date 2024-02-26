'''
Write a program that requires the user to enter a single character from the alphabet.
Print Vowel or Consonant, depending on user input.
If the user input is not a letter (between a and z or A and Z), or is a string of length > 1, print an error message.
'''
#state
user_input = input("Enter a single character from the alphabet: ")
#behavior
if len(user_input) == 1:

    if 'a' <= user_input <= 'z' or 'A' <= user_input <= 'Z':

        if user_input.lower() in ['a', 'e', 'i', 'o', 'u']:
            print("Vowel")
        else:
            print("Consonant")
    else:
        print("Error: Not a letter")
else:
    print("Error: Length should be 1")

