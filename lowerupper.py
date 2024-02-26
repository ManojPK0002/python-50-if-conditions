'''
Write a program to check whether a entered character is lowercase (a to z) or uppercase (A to Z).
'''
character=input("Enter the character")
lst=['@','#','$','%','^','&','*','1','2','3','4','5','6','7','8','9','0']
if character in lst:
    print("Invalid character")
elif character.islower():
    print("it is lowercase")
elif character.isupper():
    print("it is in uppercase")

